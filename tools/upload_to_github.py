"""在 VS Code 終端機執行：python3 upload_to_github.py --public
需要 Python 3.9+、Git、GitHub CLI (gh)。不需要 pip 安裝套件。
預設 ZIP 位於本程式旁；省略 --public 則建立私人儲存庫。
"""
import argparse
import json
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


def run(*args, cwd=None, capture=False):
    return subprocess.run(
        list(args), cwd=cwd, check=True, text=True,
        encoding="utf-8", stdout=subprocess.PIPE if capture else None,
    )


def extract_portfolio(zip_path, destination):
    """安全解壓縮，排除舊 Git 設定、hooks 及系統雜項。"""
    with zipfile.ZipFile(zip_path) as archive:
        members = archive.infolist()
        if sum(m.file_size for m in members) > 500 * 1024 * 1024:
            raise ValueError("解壓後超過 500 MB，請確認 ZIP 內容。")
        for member in members:
            path = PurePosixPath(member.filename.replace('\\', '/'))
            if path.is_absolute() or '..' in path.parts or any(':' in p for p in path.parts):
                raise ValueError("ZIP 含不安全路徑。")
            if any(p.lower() in {'.git', '__macosx', '.ds_store'} for p in path.parts):
                continue
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError("ZIP 含符號連結，已停止。")
            target = destination.joinpath(*path.parts)
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if member.file_size > 95 * 1024 * 1024:
                raise ValueError("單檔超過 95 MB，請移除大型檔案後重試。")
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as source, target.open('wb') as output:
                shutil.copyfileobj(source, output)
    if (destination / 'README.md').is_file():
        return destination
    candidates = [p for p in destination.iterdir()
                  if p.is_dir() and (p / 'README.md').is_file()]
    if len(candidates) != 1:
        raise ValueError("找不到唯一的作品集根目錄 README.md。")
    return candidates[0]


def main():
    parser = argparse.ArgumentParser(description="建立 GitHub 作品集並上傳 ZIP 內的檔案")
    parser.add_argument('--zip', type=Path,
                        default=Path(__file__).resolve().parent / '楊善茵_GitHub作品集.zip')
    parser.add_argument('--name', default='ShanYin-Engineering-Portfolio')
    parser.add_argument('--public', action='store_true', help='建立公開儲存庫（任何人可瀏覽）')
    parser.add_argument('--update', action='store_true', help='更新登入帳號下的既有儲存庫，保留其他檔案與提交歷史')
    args = parser.parse_args()
    for program in ('git', 'gh'):
        if not shutil.which(program):
            raise RuntimeError(f'找不到 {program}，請先安裝 Git 與 GitHub CLI，再重開 VS Code。')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,99}', args.name):
        raise ValueError('儲存庫名稱請使用英數字、點、底線或連字號。')
    zip_path = args.zip.expanduser().resolve()
    if not zip_path.is_file():
        raise FileNotFoundError(f'找不到壓縮檔：{zip_path}')

    # 先確認檔案可用，才進行 GitHub 登入或遠端建立。
    work = Path(tempfile.mkdtemp(prefix='github-upload-', dir=zip_path.parent))
    repo = extract_portfolio(zip_path, work)
    print(f'工作目錄：{repo}', flush=True)
    status = subprocess.run(['gh', 'auth', 'status', '--hostname', 'github.com'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if status.returncode:
        run('gh', 'auth', 'login', '--hostname', 'github.com', '--web', '--git-protocol', 'https')
    account = json.loads(run('gh', 'api', '--hostname', 'github.com', 'user', capture=True).stdout)
    owner = account['login']
    target = f'{owner}/{args.name}'
    visibility = '--public' if args.public else '--private'
    print(f'目標：{target}；模式：{"更新既有儲存庫（維持原可見範圍）" if args.update else ("新建公開儲存庫" if args.public else "新建私人儲存庫")}', flush=True)
    run('gh', 'auth', 'setup-git', '--hostname', 'github.com')
    if args.update:
        remote_copy = Path(tempfile.mkdtemp(prefix='github-update-', dir=zip_path.parent)) / 'repository'
        run('git', 'clone', '--branch', 'main', f'https://github.com/{target}.git', str(remote_copy))
        shutil.copytree(repo, remote_copy, dirs_exist_ok=True)
        repo = remote_copy
    else:
        run('git', 'init', '-b', 'main', cwd=repo)
    run('git', 'config', '--local', 'user.name', owner, cwd=repo)
    run('git', 'config', '--local', 'user.email',
        f"{account['id']}+{owner}@users.noreply.github.com", cwd=repo)
    # 移除交付備註；避免上傳後仍顯示「尚未建立」。
    (repo / 'REPOSITORY_STATUS.md').unlink(missing_ok=True)
    run('git', 'add', '.', cwd=repo)
    changed = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=repo)
    if changed.returncode == 0:
        print(f'內容已是最新版：https://github.com/{target}')
        return
    if changed.returncode != 1:
        raise RuntimeError('無法檢查暫存區差異，已停止。')
    run('git', '-c', 'commit.gpgsign=false', 'commit', '-m', 'Publish engineering portfolio', cwd=repo)
    if not args.update:
        # 新建專用：同名儲存庫已存在時 gh 會報錯，不會覆蓋既有內容。
        run('gh', 'repo', 'create', target, visibility, '--source', str(repo),
            '--remote', 'origin', '--description',
            '楊善茵｜軟體與演算法研發作品集：研究、競賽、智慧照護及證照', cwd=repo)
    run('git', 'remote', 'set-url', 'origin', f'https://github.com/{target}.git', cwd=repo)
    run('git', 'push', '-u', 'origin', 'main', cwd=repo)
    remote = run('git', 'ls-remote', 'origin', 'refs/heads/main', cwd=repo, capture=True).stdout
    local = run('git', 'rev-parse', 'HEAD', cwd=repo, capture=True).stdout.strip()
    if not remote or remote.split()[0] != local:
        raise RuntimeError('遠端版本尚未驗證成功，請保留工作目錄檢查。')
    print(f'\n上傳完成：https://github.com/{target}')
    print(f'本機副本：{repo}')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        print(f'\n未完成：{error}', file=sys.stderr)
        print('工作目錄會保留。更新既有作品集請加 --update；另建作品集可用 --name 指定新名稱。', file=sys.stderr)
        sys.exit(1)
