from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
n = 0
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    n = n + 1
    sum = sum + int(tag.contents[0])
    # Look at the parts of a tag
    print("Count",n)
    print(sum)
    