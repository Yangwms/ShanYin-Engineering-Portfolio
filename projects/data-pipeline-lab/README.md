# 資料工程環境與管線實作

**資料工程｜期中課程作業**

39 頁實作紀錄 · 環境建置、資料讀寫與工具串接

[返回作品集首頁](../../README.md)

## 技術與工具

Python / Linux / Ubuntu / Apache Airflow / Apache NiFi / PostgreSQL / Elasticsearch / Kibana

## 課程目標

資料工程期中作業，以 39 頁心得及截圖記錄教學影片 1 至 4 的實作，涵蓋 Linux 環境、資料格式、資料庫與工作流程工具。

## 環境與工具

| 工具 | 作業涵蓋內容 |
| --- | --- |
| Ubuntu 虛擬機、Java | 套件與環境準備、服務設定 |
| PostgreSQL、pgAdmin4 | 關聯式資料庫與管理介面操作 |
| Apache Airflow | 任務排程與資料管線練習 |
| Apache NiFi | 視覺化資料流、CSV／JSON 與資料庫流程 |
| Elasticsearch | 資料索引與 Python 讀寫練習 |
| Kibana | Elasticsearch 資料查詢與視覺化工具操作 |

## 資料讀寫與流程實作

1. Python 寫入及讀取 CSV，產生模擬 CSV 資料。
2. 產生及讀取 JSON，熟悉結構化資料格式。
3. 在 Airflow 建立資料管線，在 NiFi 處理 CSV／JSON。
4. 使用 Python 插入及擷取 PostgreSQL 關聯式資料。
5. 練習 Elasticsearch 資料寫入與擷取。
6. 進一步以 Airflow、NiFi 建立與資料庫互動的管線。

## 除錯與學習紀錄

作業記錄安裝失敗、服務啟動錯誤、連線設定及工具整合等問題，透過閱讀錯誤訊息、調整設定及重新測試排查。這些經驗補充了單純建模以外的環境與流程觀念；不等同正式生產環境的維運或效能保證。

## 履歷重點

- 在 Ubuntu 虛擬機環境練習服務安裝與設定，操作 PostgreSQL、pgAdmin4、Apache Airflow、Apache NiFi、Elasticsearch 與 Kibana。

- 以 Python 練習 CSV、JSON 產生與讀寫、關聯式及 Elasticsearch 資料存取，並完成 Airflow、NiFi 資料管線課程實作。

- 透過錯誤訊息與設定調整排查安裝、服務啟動及連線問題，整理實作截圖與學習紀錄。

## 成果文件與程式狀態

依個人期中作業與操作紀錄整理，屬課程環境實作；未宣稱生產環境維運、大規模吞吐效能或企業部署經驗。

目前提供的是原成果文件與技術整理，尚未提供可重現的專案原始碼、環境鎖定檔或模型權重。程式畫面不等同完整原始專案；未以新生成程式冒充過去成果。
