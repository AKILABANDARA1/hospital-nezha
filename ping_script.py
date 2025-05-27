import requests
import time

def ping_url(url, timeout=5):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        elapsed_time = time.time() - start_time
        
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {elapsed_time:.3f} seconds")
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to ping {url}")
        print(f"Error: {e}")

if __name__ == "__main__":
    ping_url("www.nezha.xx66.nyc.mn")
