import time
from datetime import datetime as dt

# Path to the hosts file (on Windows, it's usually located at C:\Windows\System32\drivers\etc\hosts)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# List of websites to block
block_list = ["www.facebook.com", "www.twitter.com", "www.instagram.com"]

def block_websites(start_hour, end_hour):
    while True:
        # Check if the current time is within the specified working hours
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in block_list:
                    if website in content:
                        pass  # Website already blocked
                    else:
                        # Add the website to the hosts file
                        file.write(redirect + " " + website + "\n")
            print("Websites blocked during working hours.")
        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    # Remove lines containing blocked websites
                    if all(website not in line for website in block_list):
                        file.write(line)
                file.truncate()
            print("Websites unblocked outside working hours.")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    # Set your working hours (24-hour format)
    start_hour = 9  # 9 AM
    end_hour = 17   # 5 PM

    block_websites(start_hour, end_hour)
