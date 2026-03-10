import requests
import sys

print("""
========================================
        IP INTELLIGENCE MODULE
========================================
Author: Divine Sunday OFUOWOICHO
========================================
""")

if len(sys.argv) != 2:
    print("Usage: python3 ip_lookup.py <ip_address>")
    print("Example: python3 ip_lookup.py 8.8.8.8")
    sys.exit()

ip = sys.argv[1]

try:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    if data["status"] == "success":

        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ZIP: {data['zip']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"Organization: {data['org']}")
        print(f"AS: {data['as']}")

    else:
        print("Lookup failed")

except:
    print("Connection error")
