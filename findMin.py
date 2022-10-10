def findmin():
    try:
        entered_list = input("Введите список чисел, разделенных пробелом: ").split()
        print("Введенный список:", entered_list)
        num_list = list(map(int, entered_list))
        print("Список чисел: ", num_list)
        print("Минимальное число: ",  min (num_list))
    except ValueError:
        print("Вы ввели не целое число")