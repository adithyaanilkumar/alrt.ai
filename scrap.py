from lxml import html
import requests
page = requests.get("https://sites.google.com/site/tomihasa/google-language-codes")
tree= html.fromstring(page.text)
data= tree.xpath('//tr//td/text()')
print(data)