import requests

def check_email(email):
    # Example using https://haveibeenpwned.com API
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": "YOUR_API_KEY_HERE"}  # Optional free API key
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Email {email} has been breached!")
        elif response.status_code == 404:
            print(f"No breaches found for {email}.")
        else:
            print("Error checking email.")
    except:
        print("Connection error.")

if __name__ == "__main__":
    email = input("Enter email to check: ")
    check_email(email)
