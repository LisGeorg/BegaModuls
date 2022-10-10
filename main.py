import indexPA
import calc
import pallindrom
import count2
import findMin
import sumnum


z = 1
while z == 1:
    print("Выберите задание: \n"
          "1)Поиска 'ра'\n"
          "2)Сложение\n"
          "3)Проверка на паллиндрому\n"
          "4)Подсчет количества двоек\n"
          "5)Нахождение наименьшего\n"
          "6)Сумма введенных чисел\n")
    number = int(input())

    if number == 1:
        indexPA.findpa()
    elif number == 2:
        calc.math()
    elif number == 3:
        pallindrom.pallindrom()
    elif number == 4:
        count2.count2()
    elif number == 5:
        findMin.findmin()
    elif number == 6:
        sumnum.sumnum()
    else:
        print("Неизвестная команда")