print("Задание3!")

InputData=[]
OutputData=[]
ListOfCosts=[]
inputlist=[]

amountofoutputdata=0
while True:
    try:
        amountofinputdata=int(input("Введите количество строк формата {ряд} {место} {стоимость билета}: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

print("Вводите билеты в формате {ряд} {место} {стоимость билета}: ")
for i in range(0,amountofinputdata):
    while True:
        try:
            InputData.append(list(map(int, input().split())))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")

for i in range(0,len(InputData)):
    if(len(OutputData)==0):
        OutputData.append(InputData[i])
    else:
        for j in range(0, len(OutputData)):
            for k in range(0,len(InputData)):
                count1=0
                if(InputData[k][0] != OutputData[j][0] or InputData[k][1] != OutputData[j][1]):
                    for l in range(0,len(OutputData)):
                        if(InputData[k][0] == OutputData[l][0] and InputData[k][1] == OutputData[l][1]):
                            count1=1
                            break
                    if(count1==1):
                        count1=0
                        break
                    else:
                        OutputData.append(InputData[k])
                #if (InputData[i][0] == OutputData[j][0] and InputData[i][1] == OutputData[j][1]):
                    #break

count=0
for i in range(0,len(OutputData)):
    count=0
    for j in range(0,len(InputData)):
       if(InputData[j][0] == OutputData[i][0] and InputData[j][1] == OutputData[i][1]):
           count=count+1
    OutputData[i].append(count)

for i in range(0,len(OutputData)):
    for j in range(0,len(InputData)):
        if (InputData[j][0] == OutputData[i][0] and InputData[j][1] == OutputData[i][1]):
            ListOfCosts.append(InputData[j][2])
    OutputData[i].append(len(set(ListOfCosts)))
    ListOfCosts=[]

print("Вывод")
for i in range(0,len(OutputData)):
    print(OutputData[i][0], ' ', OutputData[i][1], ' - ', OutputData[i][4])
