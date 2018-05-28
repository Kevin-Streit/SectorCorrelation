import csv
import math
#import os.path

print 'hello'


# Read in a pre stored CSV file open and closing marks
markReader = csv.DictReader(open('C:\Users\Kevin\Desktop\ClosingMarks\AAclose.csv', 'rb'))
markReader2 = csv.DictReader(open('C:\Users\Kevin\Desktop\ClosingMarks\Xclose.csv', 'rb'))
lineList = []
lineList2 = []

#putting each line of teh CSV in a list
#each line is a dictionaty
for line in markReader:
   lineList.append(line)
  
for line in markReader2:
   lineList2.append(line)

	
#Pulling out all of the industy titles for the list of dictionaries
#and putting them in thier own list	
AAcloseList =[]
XcloseList =[]
for item in lineList:
	AAcloseList.append(item['Close'])

for item in lineList2:
	XcloseList.append(item['Close'])
	
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

while count < (len(AAcloseList)-1):
	dailyReturnList.append((float(AAcloseList[count])/float(AAcloseList[count +1])-1))
	dailyReturnList2.append((float(XcloseList[count])/float(XcloseList[count +1])-1))
	totDailyReturn += (float(AAcloseList[count])/float(AAcloseList[count +1])-1)
	totDailyReturn2 += (float(XcloseList[count])/float(XcloseList[count +1])-1)
	count +=1

averageReturn =	totDailyReturn/(len(AAcloseList)-1)
averageReturn2 = totDailyReturn2/(len(XcloseList)-1)

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