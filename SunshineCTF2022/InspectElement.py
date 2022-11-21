import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://educashun-game.web.2022.sunshinectf.org/login.html'

x = requests.get(url,verify=False)

flag = re.findall(r"sun{.*?}", x.text)[0]

print(flag)