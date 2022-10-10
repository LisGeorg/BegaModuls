def FindPa():
    try:
        text = str(input("Введите текст: \n"))
        pa = text.find("ра")
        print(pa)
    except ValueError:
        print("Вы ввели не целое число")
