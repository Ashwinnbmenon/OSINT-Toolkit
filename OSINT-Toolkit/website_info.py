import socket

def get_website_info(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Domain: {domain}")
        print(f"IP Address: {ip}")
    except:
        print("Could not find IP address.")

if __name__ == "__main__":
    domain = input("Enter website domain (example.com): ")
    get_website_info(domain)
