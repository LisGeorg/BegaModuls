def TriangleExistenceTest():
    try:
        print ("Проверка существования треугольника")
        side_a = int (input("Введите сторону 1: "))
        side_b = int (input("Введите сторону 2: "))
        side_c = int (input("Введите сторону 3: "))
        if(side_a>side_b+side_c)or(side_b>side_a+side_c)or(side_c>side_a+side_b):
            print("Не существует")
        else:
            print("Существует")
        time.sleep(3)
    except ValueError:
        print("Вы ввели не целое число")