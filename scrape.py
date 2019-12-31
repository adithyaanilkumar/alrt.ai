import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url="https://www.autoitscript.com/autoit3/docs/appendix/OSLangCodes.htm"
html= urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'lxml')
print(soup.get_text())
tags= soup.find('td').find_all(text=True)
lst= list()
c=0
print([e.strip() for e in tags])
'''fhand = open("data.xml", "w")
for tag in tags:
    print(tag)
    fhand.write(str(tag))
    c+=1
    if c>= 50:
        break'''
'''del lst[0]
del lst[1]'''
'''for i in range(length(lst)):
    if i%4 == 0:
        del lst[i]
    elif i%5=0:
        del lst[i]'''
