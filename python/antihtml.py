import sys
import os
import re

from urllib.request import urlopen

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
    
url = str(sys.argv[1])
if url[::-1][0] == "/": 
    basename = "index.html"
else:
    basename = url.split('/')[::-1][0]

#print("Saving %s as %s" % (url,basename))
response = urlopen(url)

content = str(response.read())

stripped = remove_html_tags(content)
print(stripped)