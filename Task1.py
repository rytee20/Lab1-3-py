def find_virus(str,strvirys):
    find=0
    for i in range(0, len(str)):
        fcount = 0
        if str[i] == strvirys[0]:
            fcount = fcount + 1
            for j in range(1, len(strvirys)):
                if str[i + j] == strvirys[j]:
                    fcount = fcount + 1
                else:
                    break
        if fcount == len(strvirys):
            return 1
    return 0


def find_index_virys(str,strvirys):
    virysindex=[]
    for i in range(0, len(str)):
        fcount = 0
        if str[i] == strvirys[0]:
            fcount = fcount + 1
            for j in range(1, len(strvirys)):
                if str[i + j] == strvirys[j]:
                    fcount = fcount + 1
            if fcount == len(strvirys):
                virysindex.append(i)
    return virysindex

def delete_virys(str,strvirys, virysindex):
    for i in range(len(str) - 1, -1, -1):
        for j in range(len(virysindex) - 1, -1, -1):
            if index[j] == i:
                for k in range(0, len(strvirys)):
                    str = str[:i] + str[i + 1:]
    return str


print("Задание1!")

index = []  # список индексов первых элементов вирусов, найденных в исходной строке
count = 0  # счетчик количество совпадаемых символов
startstring = input("Введите исходную строку: ")  # вводим строку
virys = input("Введите вирус: ")  # вводим вирус
virysintheline=1

newstring = startstring.lower()  # создаем новую строку такую же как первоначальную, только все символы маленькие
virys = virys.lower()  # делаем вирус маленьким
# print(len(newstring)) проверка которая не несет смысловой нагрузки
if len(virys) > len(newstring):  # если вирус длиннее чем изначальная строка
    print("Вирус длинее, чем исходная строка")  # то как бы его нет в этой строке
else:  # иначе
    while virysintheline!=0:
        virysintheline = find_virus(newstring, virys)
        if virysintheline==1:
            index=find_index_virys(newstring,virys)
        else:
            break
        newstring=delete_virys(newstring,virys,index)
        startstring = delete_virys(startstring, virys, index)
    virysintheline=find_virus(newstring,virys)

print("Результат: ", startstring)
