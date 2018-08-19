# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

a=int(input('Enter count'))
b=int(input('Enter position'))

# Retrieve all of the anchor tags

while a is not 0:
    tags = soup('a')
    url1=tags[b-1].get('href', None)
    print(url1)
    html = urllib.request.urlopen(url1, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    a=a-1
