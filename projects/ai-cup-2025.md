# AI CUP 2025 智慧球拍辨識

**春季賽 · 團隊參與**

> 4 項分類任務 · 200+ 候選特徵

## 專案內容

- 參與「桌球智慧球拍資料的精準分析競賽」，以加速度與角速度訊號進行性別、持拍手、球齡與選手等級分類。

- 團隊比較 34 欄 baseline 與 200+ 欄增強特徵，整合時域統計、FFT 頻譜、db4 小波與感測器交互特徵。

- 以 Mutual Information 與 Random Forest 交叉驗證選擇約 50 維特徵；依任務使用 XGBoost、LightGBM、Gradient Boosting 或 SMOTE 搭配 soft voting。

## 技術

FFT / Wavelet / XGBoost / LightGBM / Random Forest

## 結果與範圍

團隊成果涵蓋特徵一致性、缺值處理、任務模型與 submission.csv 產生。未將團隊全部實作歸為個人獨立完成。

已參與競賽並有成果簡報；未提供名次證明，故不列獲獎或排名。

## 任務與模型

| 任務 | 團隊成果簡報所列模型 |
| --- | --- |
| 性別 | XGBoost |
| 持拍手 | LightGBM |
| 球齡 | SMOTE + XGBoost／LightGBM／Random Forest soft voting |
| 等級 | Gradient Boosting |

簡報第 15 頁有一次成功提交的兩個分數：0.79244267、0.7527732446625948。截圖未顯示欄名，因此本作品集不將其解讀為準確率、排名或確定的公開／私人排行榜成績。個人負責模組尚未細分，以上按團隊成果列示。

[返回作品集首頁](../README.md)
