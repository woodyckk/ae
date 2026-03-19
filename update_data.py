import requests
import json
import sys

# 醫管局官方數據接口
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    # 更加真實的偽裝 Headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8',
        'Referer': 'https://www.ha.org.hk/visitor/ha_visitor_index.asp?Content_ID=235504&Lang=CHIB5',
        'Connection': 'keep-alive'
    }

    try:
        print("🚀 開始抓取醫管局數據...")
        # 加上 verify=False 避免 SSL 證書檢查問題（有時會卡住）
        response = requests.get(url, headers=headers, timeout=30)
        
        print(f"📡 伺服器回傳狀態碼: {response.status_code}")
        
        if response.status_code == 200:
            # 先檢查內容是否為空
            if not response.text.strip():
                raise ValueError("伺服器回傳了空內容")
                
            data = response.json()
            with open('ha_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("✅ 成功產生 ha_data.json")
        else:
            print(f"❌ 抓取失敗，內容如下: {response.text[:100]}")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
