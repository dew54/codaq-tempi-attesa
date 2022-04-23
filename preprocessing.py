import datetime as dt
import numpy as np
from sklearn import datasets
import pandas as pd
import math   










def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i



def file_read(path, numberOfRows):
    indexCounter = 0
    with open(path,'r') as file:
        nRows = numberOfRows
        nColumns = 8
        dataset = np.chararray(shape=(nRows, nColumns), itemsize=10)
        for line in file:
            try:
                dataInstance = line.split(',')

                
                ticketCode = dataInstance[0]
                ticketCode = ticketCode[1:4]
                ggSett = dataInstance[1]
                arrivalDate = dataInstance[2]
                
                # if arrivalDate == "arrivalDate":
                #     pass
                # else:
                #     arrivalDate = dt.datetime.strptime(arrivalDate, '%Y-%m-%d')


                arrivalTime = dataInstance[3] #splits the line at the comma and takes the first bit
                # if arrivalTime == "arrivalTime":
                #      pass
                # else:
                #      arrivalTime = dt.datetime.strptime(arrivalTime, '%H:%M')


                waitTime = dataInstance[4]

                # if waitTime == "waitTime":
                #     pass
                # else:
                #     waitTime = dt.datetime.strptime(waitTime, '%H:%M')
                #     waitTime = int(waitTime.minute)


                serviceTime = dataInstance[5]

                # if waitTime == "waitTime":
                    
                #     pass
                # else:
                #     serviceTime = dt.datetime.strptime(serviceTime, '%H:%M')
                #     serviceTime = int(serviceTime.minute)

                ticketWaiting = dataInstance[6]
                openCounter = dataInstance[7]

                dataset[indexCounter] = [ticketCode, ggSett, arrivalDate, arrivalTime, waitTime, serviceTime, ticketWaiting, openCounter]
                indexCounter = indexCounter + 1
            except Exception as e: print(e)
                

    return dataset



rootFilePath ='C:/Users/dew54/OneDrive/Documenti/codaQ/ML/csv/'
filename = 'estrazioneFarmacia3'
fullPath = rootFilePath + filename + '.csv'

numberOfRows = file_len(fullPath) - 1

i = 0


data = file_read(fullPath, numberOfRows)



dataset = pd.DataFrame(np.array(data), columns=['ticketCode', 'ggSett', 'arrivalDate', 'arrivalTime', 'waitTime', 'serviceTime', 'ticketWaiting', 'openCounter'])

dataset = dataset.iloc[1: , :]


dataset.dropna()

print(dataset.head())

#print(numberOfRows)
rowsFirst = 0
rowsSecond = 0
rowsThird = 0
rowsFourth = 0


waitTimes = []
serviceTimes = []
numbers = []
arrivalTimes = []



for index, row in dataset.iterrows():


    try:


        waitingTime = dt.datetime.strptime(str(row[5])[2:7], '%H:%M')
        #serviceTime = dt.datetime.strptime(str(row[6])[2:7], '%H:%M')
        waitingTime = waitingTime.minute
        #serviceTime = serviceTime.minute
        dayOfMonth = row[2]
        dayOfMonth = str(dayOfMonth)
        dayOfMonth = dayOfMonth[2:12]
        dayOfMonth = dt.datetime.strptime(dayOfMonth, '%Y-%m-%d')
        dayOfMonth = dayOfMonth.day
        weekOfMonth = math.ceil(dayOfMonth/7)

        if(weekOfMonth) == 1:
            rowsFirst+=1
        elif(weekOfMonth) == 2:
            rowsSecond += 1
        elif(weekOfMonth) == 3:
            rowsThird += 1
        elif(weekOfMonth) == 4:   
            rowsFourth += 1



    except Exception as e: 
        #print(e)
        dataset.drop(index)
    
    waitTimes.append(int(waitingTime))
    serviceTimes.append(int(row[6]))


for index, row in dataset.iterrows():

    number = str(row[0])[2:5]
    arrivalTime = str(row[3])[2:7]
    numbers.append(number)
    arrivalTimes.append(arrivalTime)
    



    


firstindex = rowsFirst
secondIndex = firstindex + 1 + rowsSecond
thirdIndex = secondIndex + 1 + rowsThird
fourthIndex = thirdIndex + 1 + rowsFourth
print(dataset.head())

print(dataset.shape[0])
print(len(waitTimes))

dataset.loc[:,'waitTime'] = waitTimes
dataset.loc[:,'serviceTime'] = serviceTimes
dataset.loc[:,'ticketCode'] = numbers
dataset.loc[:,'arrivalTime'] = arrivalTimes

dataset.loc[:,'ticketWaiting'] = 5
dataset['openCounter'] = dataset['waitTime'] + dataset['serviceTime']
firstWeekDf = dataset[0:firstindex][['ticketCode', 'arrivalTime', 'waitTime' , 'serviceTime', 'openCounter']]
secondWeekDf = dataset[firstindex +1 : secondIndex][['ticketCode', 'arrivalTime', 'waitTime' , 'serviceTime', 'openCounter']]
thirdWeekDf = dataset[secondIndex+1 : thirdIndex][['ticketCode', 'arrivalTime', 'waitTime' , 'serviceTime', 'openCounter']]
fourthWeekDf = dataset[thirdIndex+1 : fourthIndex][['ticketCode', 'arrivalTime', 'waitTime' , 'serviceTime', 'openCounter']]



#print(rowsFirst)


firstWeekDf.rename(columns={"ticketCode": "Number", "arrivalTime": "Arrival time", "waitTime" : "X1", "serviceTime" : "X2", "openCounter" : "X3"},  inplace = True)
print(firstWeekDf.head())
firstWeekDf.to_csv('WEEK1.csv', index=False)
secondWeekDf.to_csv('WEEK2.csv', index=False)
thirdWeekDf.to_csv('WEEK3.csv', index=False)
fourthWeekDf.to_csv('WEEK4.csv', index=False)







        









