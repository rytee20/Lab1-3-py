print("Задание3!")

InputData=[] #входящие данные
OutputData=[] #данные для вывода
ListOfCosts=[] #список цен
inputlist=[]

amountofoutputdata=0 #количество воодимых билетов с проверкой
while True:
    try:
        amountofinputdata=int(input("Введите количество строк формата {ряд} {место} {стоимость билета}: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

print("Вводите билеты в формате {ряд} {место} {стоимость билета}: ") #ввод элементов с проверкой
for i in range(0,amountofinputdata):
    while True:
        try:
            InputData.append(list(map(int, input().split())))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")

for i in range(0,len(InputData)):
    if(len(OutputData)==0): #если в списке вывода ничего нет
        OutputData.append(InputData[i]) #добавляем первый из списка ввода
    else: #иначе
        for j in range(0, len(OutputData)): #добавление последующих элементов в список вывода, каждая пара ряд-место в списке вывода должна встречаться ровно один раз, поэтому тут много вложенных циклов для проверки
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

count=0
for i in range(0,len(OutputData)): #десь мы добавляем количество пар ряд-место в список к каждой паре в главном списке выходных данных
    count=0
    for j in range(0,len(InputData)):
       if(InputData[j][0] == OutputData[i][0] and InputData[j][1] == OutputData[i][1]):
           count=count+1
    OutputData[i].append(count)

for i in range(0,len(OutputData)): #здесь считаем количество разных цен для каждой пары ряд-место с помощью вспомогательного списка
    for j in range(0,len(InputData)):
        if (InputData[j][0] == OutputData[i][0] and InputData[j][1] == OutputData[i][1]):
            ListOfCosts.append(InputData[j][2])
    OutputData[i].append(len(set(ListOfCosts)))
    ListOfCosts=[]

print("Вывод")
for i in range(0,len(OutputData)): #вывод результата
    print(OutputData[i][0], ' ', OutputData[i][1], ' - ', OutputData[i][4])
