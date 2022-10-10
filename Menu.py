def Menu():
    try:
        print("1. Кафедра ТК:")
        print("2. Факультет")
        print("3. Каферда Радиотехника")
        ch = input("Выберите пункт: ")
        if ch == "1":
            print("\nВыбран 1 пункт\n")
        elif ch == "2":
            print("\nВыбран 3 пункт\n")
        elif ch == "3":
            print("\nВыбран 3 пункт\n")
        else:
            print("Такого нет\n")
    except ValueError:
            print("Вы ввели не целое число")
