import requests as req
from BeautifulSoup import BeautifulSoup

headers={'User-Agent':'test'}
response = req.get("https://www.uofrathletics.com/", headers=headers)
html = response.content
print html

# soup = BeautifulSoup(html)

# print soup.prettify()