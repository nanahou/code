#The code is for spider "https://www.liveatc.net/recordings.php"
#-*-coding:utf-8-*-
from lxml import etree
import requests
import urllib
url= 'https://www.liveatc.net/recordings.php'
html = requests.get(url)
print html.text

selector = etree.HTML(html.text)
content = selector.xpath('//tr[@class="d1"]/td[2]//a/@href')
count = 0
for item in content:
    count = count +1
    u = urllib.urlopen(item)
    data = u.read()
    filename = '/home/hounana/Desktop/mp3/' + str(count) + '.mp3'
    f = open(filename, 'wb')
    f.write(data)
    print u"downloading", filename
    f.close()
    print count
