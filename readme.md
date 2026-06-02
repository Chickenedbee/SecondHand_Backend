# 🔄 二手物品交換平台 (Second-Hand Exchange Platform)

本專案為一個具備安全過濾機制的二手物品交換系統。採用全端架構開發，涵蓋雲端資料庫設計、後端 API 建置與前端視覺化呈現。

## ✨ 系統特色
* **實體物品獨立登錄**：每件二手物品皆有獨立編號，確保交易真實性。
* **狀態鎖定機制**：發起交換後，系統會自動追蹤物品狀態，避免重複交易。
* **🛡️ 惡意帳號防護**：後端實作過濾邏輯，自動阻擋已被標記之停權帳號與惡意交易，保障使用者體驗。

## 🛠️ 技術架構 (Tech Stack)
* **資料庫 (Database)**：TiDB Cloud (MySQL 8.0 相容)
* **後端 (Backend)**：Python / Flask
* **前端 (Frontend)**：HTML5 / JavaScript (Fetch API) / CSS3
* **開發工具**：DBeaver, VS Code, Git

## 📂 專案檔案說明
* `schema.sql`：包含具備防護欄位 (AccountStatus, IsMalicious) 的完整資料庫架構。
* `data.sql`：包含正常使用者與惡意測試帳號之初始資料。
* `app.py`：負責連接 TiDB 並提供 `/api/exchanges` 介面的後端程式。
* `templates/index.html`：動態撈取並渲染安全交易紀錄之前端網頁。