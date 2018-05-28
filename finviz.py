import urllib
import re

openFile = open("FullStockList.txt")
lines = openFile.readlines()
FullStockList = [x.strip() for x in lines]

#stocks = ["AAL","BMY","TWTR"]
base = 'http://finviz.com/quote.ashx?t='
urls =[]


i = 0
while i<len(FullStockList):
	urls.append(base + FullStockList[i])
	i+=1
	
sector =[]
industry =[]
	
x=0	
while x < len(urls):
	grabUrl = urllib.urlopen(urls[x])

	for line in grabUrl:
		line = line.rstrip()
		if line.find('screener.ashx?v=111&f=ind') >=0 :
			dataScrape = re.findall('tab-link">(.+?)</a>', line)
			sector.append(dataScrape[0]) 
			industry.append(dataScrape[1])
	x+=1
	
openFile.close()

saveFile = open("FullSavedData.txt", 'w')
saveFile.write("Stock")
saveFile.write(",")
saveFile.write("Sector")
saveFile.write(",")
saveFile.write("Industry")
saveFile.write("\n")

n=0
while n< len(sector):
	saveFile.write(FullStockList[n])
	saveFile.write(",")
	saveFile.write(sector[n],)
	saveFile.write(",")
	saveFile.write(industry[n])
	saveFile.write("\n")
	n+=1
	
saveFile.close()

