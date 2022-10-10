def CalcOfHypoValues():
    try:
        print ("Вычисление значения гипотенузы через катеты\n")
        from math import sqrt
        cathetus1 = int (input("Введите 1 катет: "))
        cathetus2 = int (input("Введите 2 катет: "))
        print("Гипотенуза равна")
        Hypotenuse = float((sqrt(cathetus1*cathetus1+cathetus2*cathetus2)))
        print(Hypotenuse)
        time.sleep(3)
    except ValueError:
        print("Вы ввели не целое число")