import requests
import json
import sys

# 使用資料一線通 (DATA.GOV.HK) 提供的專用 JSON 連結，這對 GitHub Actions 較穩定
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    # 模擬更真實的瀏覽器指紋
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Cache-Control': 'no-cache'
    }

    try:
        print("🚀 嘗試從 HA Open Data 接口抓取...")
        # 加上 allow_redirects=True 確保跟隨跳轉
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        
        print(f"📡 狀態碼: {response.status_code}")
        
        # 檢查是否為有效的 JSON 格式
        try:
            data = response.json()
            # 驗證關鍵字，確保不是抓到錯誤頁面的 JSON
            if 'waitTime' in data:
                with open('ha_data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print("✅ 數據同步成功！已儲存至 ha_data.json")
            else:
                print("⚠️ 抓取成功但資料格式不符預期。")
                sys.exit(1)
        except ValueError:
            print("❌ 抓取失敗：回傳內容不是 JSON。")
            print("內容開頭為：", response.text[:100])
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 網路連線錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
