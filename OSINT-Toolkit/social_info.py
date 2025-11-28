def get_social_info(username):
    print(f"Gathering public info for {username}...")
    # Simulated example
    print(f"Twitter: https://twitter.com/{username}")
    print(f"Instagram: https://instagram.com/{username}")
    print(f"LinkedIn: https://linkedin.com/in/{username}")

if __name__ == "__main__":
    username = input("Enter username: ")
    get_social_info(username)
