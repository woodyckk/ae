import requests
import json

# 醫管局官方數據接口
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

try:
    # 模擬瀏覽器請求，避免被擋
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, timeout=15)
    
    if response.status_code == 200:
        data = response.json()
        # 存成本地 JSON 檔案
        with open('ha_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("✅ 數據抓取並儲存成功")
    else:
        print(f"❌ 抓取失敗，狀態碼: {response.status_code}")
except Exception as e:
    print(f"❌ 發生錯誤: {e}")
