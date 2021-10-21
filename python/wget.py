import sys
import os
from urllib.request import urlopen

url = str(sys.argv[1])
if url[::-1][0] == "/": 
    basename = "index.html"
else:
    basename = url.split('/')[::-1][0]

print("Saving %s as %s" % (url,basename))
response = urlopen(url)

content = response.read()

c = open(basename, 'w')

c.write(str(content))
c.close
