print("Бонус!")
while True:
    try:
        countofmagic=int(input("Введите номер магического числа: "))
        break
    except ValueError:
        print("Попробуйте снова: ")

count=0 #счетчик магического числа

while count!=countofmagic:
    if (len(str(i)) == 2 and ((i % 10) + (i // 10)) == 10):  # если двузначное и сумма всех цифр =10
        count = count + 1  # счетчик +1
    else:
        if (len(str(i)) == 3 and (
                (i % 10) + (i // 10) % 10 + (i // 100)) == 10):  # если трехзначное и сумма всех цифр =10
            count = count + 1  # счетчик +1
        else:
            if (len(str(i)) == 4 and ((i % 10) + (i // 10) % 10 + (i // 100) % 10 + (
                    i // 1000)) == 10):  # если четырехзначное и сумма всех цифр =10
                count = count + 1  # счетчик +1

    if(count==countofmagic): #сли счетчик совпадает с введеным номером
        print("Магическое число: ", i) #выводим
        break #выходим из цикла
