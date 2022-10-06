def findzero(listofnumbers): #фунция ищет количество 0
    count=0 #счетчик нулей
    for i in range(0,len(listofnumbers)): #перебираем все элементы
        if listofnumbers[i]==0: #если элемент =0
            count=count+1 #счетчик+1
    return count #возвращаем счетчик

def minusoneifnozero(listofnumbers): #функция отнимает 1 от всех элементов, если нет 0 в последовательности, возвращает новый список
    for i in range(0,len(listofnumbers)): #перебираем элементы
        listofnumbers[i] = listofnumbers[i] - 1 #каждый элемент -1
    return listofnumbers #возвращаем получившийся список

def minusoneifzero(listofnumbers): #функция отнимает 1 от чисел, если есть 0 в последовательности, возвращает новый список
    defcountofoperations=0 #количество операций в функции
    for i in range(len(listofnumbers) - 1, -1, -1):
        if listofnumbers[i]!=0: #если элемент !=0
            if i==0 or listofnumbers[i-1]==0: #если это первый элемент в списке или если предыдущий был равен нулю
                listofnumbers[i] = listofnumbers[i] - 1 #элемент-1
                defcountofoperations = defcountofoperations + 1 #количество операций +1
            else:
                listofnumbers[i] = listofnumbers[i] - 1
    return listofnumbers, defcountofoperations #возвращаем список и количество операций

print("Задание2!")

amountofnumbers=4
numbers=[]*amountofnumbers #список чисел
amountofzeros=0 #количество 0
countofoperations=0 #счетчик операций
countofoperations1=0 #счетчик1

print("Количество вводимых чисел=4, введите 4 числа через пробел")


while True: #ввод чисел через пробел
    try:
        numbers=list(map(int, input().split()))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

for i in range(0,len(numbers)): #печать для проверки введеных чисел
    print(numbers[i])

while amountofzeros!=amountofnumbers: #пока количесво операций не равно количеству нулей
    amountofzeros=findzero(numbers) #считаем количество нулей
    if amountofzeros==amountofnumbers: #если равны, выходим из цикла
        break
    else: #иначе
        if amountofzeros==0: #если количество нулей равно 0
            numbers=minusoneifnozero(numbers) #отнимаем по 1 и возвращаем новый список
            countofoperations=countofoperations+1 #увеличиваем количество операций
        else: #иначе
            numbers,countofoperations1=minusoneifzero(numbers) #отнимаем по 1 и возвращаем новый список и количество операций произошедших внутри функции
            countofoperations=countofoperations+countofoperations1 #складываем количество опрераций

print("Количество операций: ", countofoperations) #вывод количества операций
