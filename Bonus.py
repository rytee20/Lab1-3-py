print("Бонус!")

countofmagic=int(input("Введите номер магического числа: "))
count=0

for i in range (1,10000):
    if(len(str(i))==2 and ((i%10)+(i//10))==10):
        count=count+1
    else:
        if(len(str(i))==3 and ((i%10)+(i//10)%10+(i//100))==10):
            count = count + 1
        else:
            if(len(str(i))==4 and ((i%10)+(i//10)%10+(i//100)%10+(i//1000))==10):
                count = count + 1
    if(count==countofmagic):
        print("Магическое число: ", i)
        break
