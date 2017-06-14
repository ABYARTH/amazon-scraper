#import socks
#import socket
#
#import stem.process
#
#SOCKS_PORT=7000# You can change the port number
#
#tor_process = stem.process.launch_tor_with_config(
#    config = {
#        'SocksPort': str(SOCKS_PORT),
#    },
#)
#
#
#socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=SOCKS_PORT)
#
#socket.socket = socks.socksocket

from bs4 import BeautifulSoup
import urllib

arr = []
keyword = "samsung"
for i in range(1,10):
    i = str(i)
    url = "http://www.amazon.in/s/ref=sr_pg_"+i+"?rh=n%3A976419031%2Ck%3A"+keyword+"&page="+i+"&keywords="+keyword

    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)

    content = soup.find_all("a", class_="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal")

#    print content

    for c in content:
        try:
            label = c.get('href')
            sublabel = label.split("/")

            print sublabel

            arr.append(sublabel[5])

        except:
            pass

#print arr

title_arr = []

for i in range(0, len(arr)):
    try:
        uri = "http://www.amazon.in/dp/"+arr[i]+"/"
        dt = urllib.urlopen(uri).read()
        cont = BeautifulSoup(dt)

        content = cont.find_all("span", class_="a-size-large")
        for conte in content:
            p = conte.text.strip()
#            print p
            title_arr.append(p)
    except:
        pass

print title_arr    
    
#tor_process.kill()