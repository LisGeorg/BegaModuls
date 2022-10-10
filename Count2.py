def Count2():
    try:
        entered_list = input("Введите список чисел, разделенных пробелом: ").split()
        num_list = list(map(int, entered_list))
        print("Список чисел: ", num_list)
        element_count = len([item for item in num_list if item == 2])
        print("Количество двоек:", element_count)
    except ValueError:
        print("Вы ввели не целое число")
