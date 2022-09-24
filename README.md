# Lab1-3-py
1 лаба, 3 семестр, 1 вариант, Python

Задание №1. 
----------
Пользователь с клавиатуры вводит две строки s и x, где s –
исходная строка, x – «вирус». Необходимо из исходной строки s удалить все 
вхождения строки x, таким образом, чтобы в результирующей строке не 
осталось «вирусов».  
Строки не чувствительны к регистру!

Задание №2.
-----------
Пользователь с клавиатуры вводит n целых положительных чисел 
(через пробел) – получаем список an. Вам доступна следующая операция:
* выберите отрезок [ai, aj], такой, что 1 ⩽ i ⩽ j ⩽ n
* уменьшите элементы ai, ai+1, ai+2, … , aj на единицу  
Задача вывести число k – минимальное количество операций, после которых 
все элементы списка будут равны нулю.

Задание №3.
----------
Администратору кинотеатра необходимо вести учёт стоимости билетов. Цена
на билет в различные дни/часы может изменяться, поэтому для пары ряд/место, 
может быть задано несколько строк.  
Входные данные:
Пользователь вводит целое положительное число n – количество строк.  
Затем вводит n строк формата:  
{ряд} {место} {стоимость_билета}  
Например, строка   
1 2 1000   
означает: 1-й ряд, 2 место, 1000 руб.  
Выходные данные:  
m пар {рядi} {местоi} – {ki}  
где ki – количество различных возможных цен билета на {рядi} {местоi}

Бонус
-----
Будем называть положительное целое число «магическим», если сумма его цифр 
равна 10. Вам дано целое число k, найдите k-е по величине прекрасное «магическое» 
целое число.  
Входные данные:  
Пользователь вводит целое число k (1 ≤ k ≤ 10000).  
Выходные данные:  
Выведите k-е по величине «магическое» число.
