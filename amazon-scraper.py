from bs4 import BeautifulSoup
import urllib
from time import sleep
import csv

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def scrape():
	arr = []
	keyword = "samsung"
	for i in range(1,30):
	    i = str(i)
	    url = "http://www.amazon.in/s/ref=sr_pg_"+i+"?rh=n%3A976419031%2Ck%3A"+keyword+"&page="+i+"&keywords="+keyword

	    r = urllib.urlopen(url).read()
	    soup = BeautifulSoup(r)

	    content = soup.find_all("a", class_="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal")

	    for c in content:
		try:
		    label = c.get('href')
		    sublabel = label.split("/")
		    arr.append(sublabel[5])
		except:
		    pass

	title_arr = []

	for i in range(0, len(arr)):
	    try:
			sleep(0.5)
			uri = "http://www.amazon.in/dp/"+arr[i]+"/"
			dt = urllib.urlopen(uri).read()
			cont = BeautifulSoup(dt)

			content = cont.find_all("span", class_="a-size-large")
			for conte in content:
			    p = conte.text.strip()
			    if (p != '+'):
			    	title_arr.append(p)
			    if len(title_arr) == 10:
			    	break
	    except:
			pass

	print title_arr

	datafile = open('datafile.csv', 'wb')
	fieldnames = ['products']
	writer = csv.DictWriter(datafile, fieldnames=fieldnames)
	writer.writeheader()
	for r in title_arr:
		writer.writerow({'products': r.encode("utf-8")})
	datafile.close()


scrape()
