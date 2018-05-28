import csv
import math

cmarkReader = csv.DictReader(open('C:\Users\Kevin\Desktop\ClosingMarks\SPYclose.csv','rb'))
cmarkReader2 = csv.DictReader(open('C:\Users\Kevin\Desktop\ClosingMarks\DIAclose.csv','rb'))
stockCloseList = []
closeList =[]
stockCloseList2 = []
closeList2 =[]

for line in cmarkReader:
	stockCloseList.append(line)

for line in cmarkReader2:
	stockCloseList2.append(line)

for item in stockCloseList:
	closeList.append(item['Close'])
	
for item in stockCloseList2:
	closeList2.append(item['Close'])

dailyReturnList = []
dailyReturnList2 = []
coVar =[]
coVar2 =[]


count = 0
totDailyReturn = 0
totDailyReturn2 = 0
diffSquared = 0
diffSquared2 = 0
#coVar=0
#coVar2=0

while count < (len(closeList)-1):
	dailyReturnList.append((float(closeList[count])/float(closeList[count +1])-1))
	dailyReturnList2.append((float(closeList2[count])/float(closeList2[count +1])-1))
	totDailyReturn += (float(closeList[count])/float(closeList[count +1])-1)
	totDailyReturn2 += (float(closeList2[count])/float(closeList2[count +1])-1)
	count +=1

averageReturn =	totDailyReturn/(len(closeList)-1)
averageReturn2 = totDailyReturn2/(len(closeList)-1)

print averageReturn
print averageReturn2

#covarience formula 1/(n-1)E(Xi-Xavg)(Yi-Yavg)
for item in dailyReturnList:
	diffSquared += (float(item) - averageReturn)**2
	coVar.append(float(item) - averageReturn)

for item in dailyReturnList2:
	diffSquared2 += (float(item) - averageReturn2)**2
	coVar2.append(float(item) - averageReturn2)

#print coVar
total = 0.0
for i in range(0, len(coVar)):
	total += (coVar[i]*coVar2[i])

covarience = total/len(coVar)
	
print covarience

varience = diffSquared/len(dailyReturnList)
varience2 = diffSquared2/len(dailyReturnList2)
stdDev = math.sqrt(varience)
stdDev2 = math.sqrt(varience2)

correlation = covarience/(stdDev*stdDev2)

print "Final Correelation is: ", correlation

	

