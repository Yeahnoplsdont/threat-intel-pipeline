import requests
import urllib3
import csv
urllib3.disable_warnings()

API_KEY = "your_api_key_here"

ips = [
    "100.23.75.120",
    "101.200.77.117",
    "101.200.96.234",
    "101.201.226.38",
    "101.201.233.222",
    "101.47.28.226",
    "101.96.192.45",
    "102.210.148.203",
    "103.24.212.42",
    "103.28.16.162",
]

url = "https://api.abuseipdb.com/api/v2/check"
headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}

results = []

for ip in ips:
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    response = requests.get(url, headers=headers, params = params , verify=False)
    data = response.json()['data']

    results.append({
        'ip': ip,
        'score': data['abuseConfidenceScore'],
        'reports': data['totalReports'],
        'isp': data['isp'],
        'usage': data['usageType'],
        'country': data['countryCode'],
        'isTor': data['isTor'],
        'isWhitelisted': data['isWhitelisted']
    })

with open('results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("Done. Results saved to results.csv")
