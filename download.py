import urllib

openFile = open("FullStockList2.txt")
lines = openFile.readlines()
stockList = [x.strip() for x in lines]

Stocks = ['DAL','BBRY']

startUrl = 'http://chart.finance.yahoo.com/table.csv?s='
endUrl = '&a=8&b=27&c=2016&d=9&e=27&f=2016&g=d&ignore=.csv'

count = 0
for stock in Stocks:
	download = urllib.URLopener()
	try:
		download.retrieve(startUrl + Stocks[count] + endUrl, Stocks[count]+"close.csv")
		count +=1
	except IOError as e: 
		print e
