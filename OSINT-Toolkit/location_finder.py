import requests

def get_ip_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(f"IP: {ip}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
    except:
        print("Could not retrieve location.")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    get_ip_location(ip)
