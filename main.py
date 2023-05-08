import requests
from datetime import datetime
response = requests.get("https://www.httpbin.org/ip")
json_response = response.json()
origin = json_response.get("origin")


# Appending to ip.txt
with open("ip.txt", "a") as file:
    file.write(origin + "\t" + str(datetime.now()) + "\n")

