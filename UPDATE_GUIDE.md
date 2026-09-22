# 更新 GitHub 作品集

這份 ZIP 是作品集的新版內容。程式會解壓縮後更新 GitHub 中的個別檔案，使 README 首頁與專案連結直接可讀，不是只上傳 ZIP 檔。

## 已有作品集的 Mac 使用者

1. 下載新版 `楊善茵_GitHub作品集.zip` 與新版 `upload_to_github.py`，放在 `/Users/jojo/Desktop/github`。
2. 取代同名舊檔，保留上述檔名；避免下載後變成帶有 `(1)` 的名稱。
3. ZIP 不必手動解壓。在 VS Code 終端機執行：

```bash
cd /Users/jojo/Desktop/github
/usr/local/bin/python3.12 upload_to_github.py --update
```

程式會讀取目前 GitHub CLI 登入帳號，更新其 `ShanYin-Engineering-Portfolio` 儲存庫的 main 分支。過程會複製遠端儲存庫到新的本機資料夾、套用新版檔案、建立提交並 push，最後確認遠端提交一致。既有可見範圍及歷史會保留；壓縮檔未涵蓋的其他檔案不會被批次刪除。

若你先前更改過儲存庫名稱，請改用：

```bash
/usr/local/bin/python3.12 upload_to_github.py --update --name 你的儲存庫名稱
```

## 只有 ZIP 時

手動解壓後，可在解壓縮資料夾找到 `tools/upload_to_github.py`。執行時以 `--zip` 指定原 ZIP 的完整路徑，例如：

```bash
/usr/local/bin/python3.12 tools/upload_to_github.py --update --zip /Users/jojo/Desktop/github/楊善茵_GitHub作品集.zip
```

## 尚未建立 GitHub 儲存庫

僅在遠端尚未建立的情況使用下列命令，建立公開作品集：

```bash
/usr/local/bin/python3.12 upload_to_github.py --public
```

## 登入與常見訊息

- `gh` 找不到：先安裝 GitHub CLI；`brew install gh`。
- 登入授權：終端機 `One-time code` 那一行就是設備驗證碼，不會另寄信。依提示按 Enter 開啟瀏覽器並貼上新代碼。
- `expired_token`：重新執行取得新代碼，舊碼無法使用。
- `repository not found`：確認登入帳號與儲存庫名稱；若只有完成登入，尚未建立儲存庫，使用前節的新建命令。
- `內容已是最新版`：本次無檔案差異，不需重複提交。
- 若 push 被拒絕：保留錯誤訊息與工作目錄，不要使用 force push；重新執行更新可從最新遠端重新套用。

完成後開啟終端機顯示的 GitHub 網址，重新整理頁面。新版首頁應有九個專案，包含人工智慧課程的視障友善導引提案；台股研究以單日與五日方法說明。

## 程式碼範圍

`tools/` 中的 Python 程式是本次作品集整理與維護工具，不是原課程／研究程式。專案原始碼尚未提供，成果頁不宣稱具有完整可重現環境。
