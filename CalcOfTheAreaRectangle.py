def CalcOfTheAreaRectangle():
    try:
        print("Вычисление площади прямоугольника\n")
        length = int(input("Введите длину:"))
        width = int(input("Введите ширину:"))
        print("Площадь равна:")
        square = (length * width)
        print(square)
        time.sleep(3)
    except ValueError:
        print("Вы ввели не целое число")