import requests
import json
import sys

# 改用資料一線通 (DATA.GOV.HK) 的官方轉發網址，這對自動化程式最友好
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    try:
        print("🚀 正在從官方 API 抓取數據...")
        response = requests.get(url, headers=headers, timeout=30)
        
        # 檢查內容是否真的抓到了 JSON
        if response.status_code == 200:
            try:
                data = response.json()
                # 額外檢查：確保資料夾中有 waitTime 這個 Key
                if 'waitTime' in data:
                    with open('ha_data.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    print("✅ 數據解析成功！ha_data.json 已更新。")
                else:
                    print("❌ 抓取成功但格式不符。")
                    sys.exit(1)
            except Exception:
                print("❌ 抓到的是網頁內容而非 JSON。內容開頭：")
                print(response.text[:100])
                sys.exit(1)
        else:
            print(f"❌ 伺服器回傳狀態碼: {response.status_code}")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 連線失敗: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
