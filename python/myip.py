import sys
import os
import json
from urllib.request import urlopen

url = "http://httpbin.org/get"
res = urlopen(url)

content = json.loads(str(res.read()))


