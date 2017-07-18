import urllib2
import zlib
import json

Linkarr = []

def grablinks():
	url = "http://www.awesummly.com/api/india/notifications/?audio=true"
	hedr = {
				'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Encoding':	'gzip, deflate',
				'Accept-Language':	'en-US,en;q=0.5',
				'Connection':	'keep-alive',
				'Cookie':	'__cfduid=d4bc1ad25bf8d5b8d8396f4045ac80a861500290619; _ga=GA1.2.953613925.1500297451; __auc=dbab5f9015d50b25707a82bea96',
				'Host':	'www.awesummly.com',
				'Upgrade-Insecure-Requests':	'1',
				'User-Agent':	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
			}

	u = urllib2.Request(url, headers = hedr)
	page = urllib2.urlopen(u)

	decompressed_dataa=zlib.decompress(page.read(), 16+zlib.MAX_WBITS)
	# print decompressed_dataa
	decompressed_data = json.loads(decompressed_dataa)
	# decompressed_data = decompressed_dataa
	sedata = decompressed_data['contents']
	for ddata in sedata:
		for k in ddata['audios'].itervalues():
			print k
			Linkarr.append(k)

	grabfile()		

def grabfile():
	for onelink in Linkarr:
		url = onelink
		file_name = url.split('/')[-1]
		u = urllib2.urlopen(url)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
		    buffer = u.read(block_sz)
		    if not buffer:
		        break

		    file_size_dl += len(buffer)
		    f.write(buffer)
		    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		    status = status + chr(8)*(len(status)+1)
		    print status,

		f.close()

grablinks()