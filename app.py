from flask import Flask, jsonify, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
# 讓首頁直接顯示我們剛做好的 HTML 網頁
@app.route('/')
def home():
    return render_template('index.html')
  
# 1. 資料庫連線設定 (請替換成您的專屬資訊)
db_config = {
    'host': 'gateway01.ap-northeast-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': '防止個資外洩.root',      # 例如: 2rCEeJ6hM6Nw2Et.root
    'password': '防止個資外洩',      # TiDB 產生的那串密碼
    'database': 'SecondHandExchange',
    'ssl': {'ssl': {}}               # 這是關鍵！TiDB 雲端強制要求 SSL 加密
}

# 2. 建立一個 API 路由：取得乾淨的交易紀錄
@app.route('/api/exchanges', methods=['GET'])
def get_safe_exchanges():
    # 建立資料庫連線
    connection = pymysql.connect(**db_config)
    
    try:
        # 使用 DictCursor 讓撈出來的資料變成「字典」格式，網頁才看得懂
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            
            # 這裡就是我們剛剛在 DBeaver 測試成功的「惡意過濾」語法！
            sql = """
                SELECT 
                    ExchangesID AS '交換編號', 
                    ProposerUserID AS '發起人編號', 
                    OrderDate AS '發起時間', 
                    Status AS '交易狀態'
                FROM Exchanges 
                WHERE IsMalicious = FALSE;
            """
            cursor.execute(sql)
            records = cursor.fetchall()
            
            # 將結果打包成 JSON 格式回傳
            return jsonify({
                "status": "success",
                "message": "成功取得交易紀錄（已過濾惡意行為）",
                "data": records
            })
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
        
    finally:
        # 確保連線用完後有安全關閉
        connection.close()

# 3. 啟動伺服器
if __name__ == '__main__':
    print("🚀 後端伺服器啟動中...")
    app.run(debug=True, port=5000)
