# AI CUP 2025 智慧球拍辨識

**春季賽 · 團隊參與**

4 項分類任務 · 200+ 候選特徵

[返回作品集首頁](../../README.md)

## 技術與工具

FFT / Wavelet / XGBoost / LightGBM / Random Forest

## 競賽問題

AI CUP 2025 春季賽「桌球智慧球拍資料的精準分析競賽」。團隊以 Ax、Ay、Az 加速度與 Gx、Gy、Gz 角速度資料，處理性別、持拍手、球齡與選手等級四個分類任務。

## 特徵與選擇流程

比較 34 欄 baseline 與 200 多欄候選特徵。特徵包含時域統計、FFT 頻譜、db4 小波及感測器間交互資訊；先以 Mutual Information 篩選約 80 個，再以 Random Forest 交叉驗證選出約 50 維特徵。

## 任務模型

| 任務 | 團隊簡報使用方法 |
| --- | --- |
| 性別 | XGBoost |
| 持拍手 | LightGBM |
| 球齡 | SMOTE 與 XGBoost、LightGBM、Random Forest soft voting |
| 選手等級 | Gradient Boosting |

## 交付與成果範圍

團隊處理特徵一致性、缺值與預測提交流程，產出競賽 submission.csv。楊善茵以團隊成員身分參與；沒有提供可驗證名次，不列獲獎，簡報中未明確標註意義的分數亦不改稱準確率。

## 履歷重點

- 參與「桌球智慧球拍資料的精準分析競賽」，以加速度與角速度訊號進行性別、持拍手、球齡與選手等級分類。

- 團隊比較 34 欄 baseline 與 200+ 欄增強特徵，整合時域統計、FFT 頻譜、db4 小波與感測器交互特徵。

- 以 Mutual Information 與 Random Forest 交叉驗證選擇約 50 維特徵；依任務使用 XGBoost、LightGBM、Gradient Boosting 或 SMOTE 搭配 soft voting。

## 成果文件與程式狀態

團隊成果涵蓋特徵一致性、缺值處理、任務模型與 submission.csv 產生。未將團隊全部實作歸為個人獨立完成。

目前提供的是原成果文件與技術整理，尚未提供可重現的專案原始碼、環境鎖定檔或模型權重。程式畫面不等同完整原始專案；未以新生成程式冒充過去成果。
