def findzero(listofnumbers):
    count=0
    for i in range(0,len(listofnumbers)):
        if listofnumbers[i]==0:
            count=count+1
    return count

def minusoneifnozero(listofnumbers):
    for i in range(0,len(listofnumbers)):
        listofnumbers[i] = listofnumbers[i] - 1
    return listofnumbers

def minusoneifzero(listofnumbers):
    defcountofoperations=0
    for i in range(0,len(listofnumbers)):
        if listofnumbers[i]!=0:
            if i==0 or listofnumbers[i-1]==0:
                listofnumbers[i] = listofnumbers[i] - 1
                defcountofoperations = defcountofoperations + 1
    return listofnumbers, defcountofoperations

print("Задание2!")

amountofnumbers=int(input("Введите колтчество чисел: "))
numbers=[]
amountofzeros=0
countofoperations=0
countofoperations1=0

for i in range(0,amountofnumbers):
    numbers.append(int(input("Введите число: ")))

for i in range(0,len(numbers)):
    print(numbers[i])

while amountofzeros!=amountofnumbers:
    amountofzeros=findzero(numbers)
    if amountofzeros==amountofnumbers:
        break
    else:
        if amountofzeros==0:
            numbers=minusoneifnozero(numbers)
            countofoperations=countofoperations+1
        else:
            numbers,countofoperations1=minusoneifzero(numbers)
            countofoperations=countofoperations+countofoperations1

print("Количество операций: ", countofoperations)
