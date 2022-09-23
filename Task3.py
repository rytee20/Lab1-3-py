print("Задание3!")

InputData=[]
OutputData=[]
ListOfCosts=[[0]*100]*100
#count=1

amountofoutputdata=0
amountofinputdata=int(input("Введите количество строк формата {ряд} {место} {стоимость билета}: "))

print("Вводите билеты в формате {ряд} {место} {стоимость билета}: ")
for i in range(0,amountofinputdata):
    InputData.append(input().split(' '))

for i in range(0,amountofinputdata):
    if(len(OutputData)==0):
        OutputData.append(InputData[i])
        #OutputData[0][2] = count
        #amountofoutputdata=amountofoutputdata+1
    else:
        count=1
        for j in range(0,len(OutputData)):
            if(InputData[i][0] == OutputData[j][0] and InputData[i][1] == OutputData[j][1]):
                count = count + 1
                #OutputData[j][2] = count
        for j in range(0, len(OutputData)):
            if (InputData[i][0] == OutputData[j][0] and InputData[i][1] == OutputData[j][1]):
                break
            if(InputData[i][0] != OutputData[j][0] and InputData[i][1] != OutputData[j][1]):
                OutputData.append(InputData[i])
                #OutputData[j][2] = count

count=0
for i in range(0,len(OutputData)):
    count=0
    for j in range(0,len(InputData)):
       if(InputData[j][0] == OutputData[i][0] and InputData[j][1] == OutputData[i][1]):
           count=count+1
    OutputData[i][2]=count

count=0
for i in range(0,len(OutputData)):
    count = 0
    for j in range(0,len(InputData)):
        if (InputData[j][0] == OutputData[i][0] and InputData[j][1] == OutputData[i][1]):
            ListOfCosts[i][count]=InputData[j][2]
            count = count + 1

print("Вывод")
for i in range(0,len(OutputData)):
    print(OutputData[i])
    print(ListOfCosts[i])
