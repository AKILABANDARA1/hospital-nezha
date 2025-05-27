import requests
import time

def ping_url(url, timeout=5):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        elapsed_time = time.time() - start_time
        
        print(f"[{time.ctime()}] URL: {url}")
        print(f"[{time.ctime()}] Status Code: {response.status_code}")
        print(f"[{time.ctime()}] Response Time: {elapsed_time:.3f} seconds\n")
        
    except requests.exceptions.RequestException as e:
        print(f"[{time.ctime()}] Failed to ping {url}")
        print(f"[{time.ctime()}] Error: {e}\n")

if __name__ == "__main__":
    url = "https://nezha.xx66.nyc.mn/"  # Use HTTPS here, not just www

    while True:
        print(f"Starting 4 pings to {url} at {time.ctime()}")
        for _ in range(4):
            ping_url(url)
            time.sleep(1)  # Short pause between each ping (optional)
        
        print(f"Sleeping for 6 hours...\n")
        time.sleep(21600)  # 6 hours = 21600 seconds
