import random
import time

def getRandomDate(startDate, endDate ):
    print("Printing random date beetween", startDate, "and", endDate)
    randomGenorator = random.random()
    print(f"Random Genorator {randomGenorator}")
    dateFormat = "%m/%d/%Y"
    print("Strptime output is : ", time.strptime(startDate, dateFormat))
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenorator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))
