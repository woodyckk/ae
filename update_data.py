import requests
import json
import sys

# 官方 Open Data 接口
url = "https://www.ha.org.hk/opendata/aewaitingtime/aewaitingtime-tc.json"

def fetch_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8',
        'Referer': 'https://www.ha.org.hk/',
        'Origin': 'https://www.ha.org.hk'
    }

    try:
        print("🚀 正在嘗試繞過阻擋抓取數據...")
        # 加上 timeout 防止無限等待
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            # 存成檔案，供 index.html 讀取
            with open('ha_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("✅ 成功產生 ha_data.json！")
        else:
            print(f"❌ 抓取失敗，狀態碼: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
