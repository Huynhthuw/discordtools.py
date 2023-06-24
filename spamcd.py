import requests
import time

time.sleep(20)

payload = {
   'content': "#put your messenge here"
}

header = {
    'authorization': '#here'
}
for i in range(200):
    r = requests.post('#here', data=payload, headers=header)
    time.sleep(20)
