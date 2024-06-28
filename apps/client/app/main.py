import requests
import time
import os

def fetch_endpoint(endpoint):
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            print(f"{endpoint} endpoint response:", response.json())
        else:
            print(f"Failed to fetch {endpoint} endpoint, status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {endpoint} endpoint:", e)

def main():
    endpoints_str = os.getenv('ENDPOINTS')
    if not endpoints_str:
        print("No endpoints defined in the environment variables.")
        return
    endpoints = endpoints_str.split(',')
    while True:
        for endpoint in endpoints:
            fetch_endpoint(endpoint)
        print("sleeping for 30 seconds")
        time.sleep(30)

if __name__ == "__main__":
    main()
