from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


#open url and read html code
opn = urlopen("https://github.com/")
rd = opn.read()
ans = rd.decode("utf-8")
print(ans)

# take image url from given website url 
opn = urlopen('https://www.shutterstock.com/search/bmw')
cvn_bs = BeautifulSoup(opn, 'html.parser')
jpg = cvn_bs.find_all('img',{'src':re.compile('.jpg')})
for i in jpg:
    print(i['src'],'\n')


# take title from html 
ur = requests.get("https://github.com/")
take = BeautifulSoup(ur.content, 'html.parser')
url_title = take.select('title')[0].text
print(url_title)

# take first heading from html  
fl = requests.get("https://github.com/")
takefl = BeautifulSoup(fl.content, 'html.parser')
url_fl = takefl.select('h1')[0].text
print(url_fl)


