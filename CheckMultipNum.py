def CheckMultipNum():
    try:
        print ("Проверка кратности числа")
        variable7 = int (input("Введите число: "))
        divider = int (input("Введите делитель: "))
        if (variable7%divider == 0):
            print ("Кратное")
        else:
            print ("Не кратное")
        time.sleep(3)
    except ValueError:
        print("Вы ввели не целое число")
        time.sleep(3)