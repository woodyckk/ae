import requests
import json
import sys

# 使用 AllOrigins 中轉服務來繞過醫管局對 GitHub Actions IP 嘅直接封鎖
proxy_url = "https://api.allorigins.win/get?url="
target_url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    try:
        print("🚀 正在透過中轉伺服器抓取數據...")
        # 透過中轉站請求，避開直接連線
        response = requests.get(f"{proxy_url}{target_url}", timeout=30)
        
        if response.status_code == 200:
            # AllOrigins 會將結果包裝喺 'contents' 入面
            raw_data = response.json()
            content_str = raw_data.get('contents')
            
            if content_str:
                data = json.loads(content_str)
                with open('ha_data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print("✅ 數據同步成功！ha_data.json 已更新。")
            else:
                print("❌ 中轉站回傳內容為空。")
                sys.exit(1)
        else:
            print(f"❌ 中轉站回傳狀態碼: {response.status_code}")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
