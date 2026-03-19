import requests
import json
import sys

# 這是「資料一線通」提供的官方 API 接口，專門給程式讀取的
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        print("🚀 正在從資料一線通抓取數據...")
        # 這是關鍵：我們改用這個穩定的 URL
        response = requests.get(url, headers=headers, timeout=30)
        
        print(f"📡 狀態碼: {response.status_code}")
        
        # 試著解析 JSON，如果失敗就印出內容看看是什麼
        try:
            data = response.json()
            with open('ha_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("✅ 數據抓取成功！ha_data.json 已更新。")
        except Exception:
            print("❌ 內容不是有效的 JSON，抓到的內容開頭是：")
            print(response.text[:200]) # 印出前 200 字檢查是不是抓到了 HTML
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 連線發生錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
