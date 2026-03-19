import requests
import json
import sys

# 醫管局官方數據接口
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            # 確保檔案一定會被寫入
            with open('ha_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("✅ 成功產生 ha_data.json")
        else:
            print(f"❌ 抓取失敗，狀態碼: {response.status_code}")
            sys.exit(1) # 強制報錯讓 GitHub 知道
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
