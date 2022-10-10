def CalcAreaTriangleHeightBase():
    try:
        print("Вычисление площади треугольника через высоту и основание")
        footing =int(input("Введите основание\n"))
        height =int(input("Введите высоту\n"))
        square =int ((1/2)*footing*height)
        print("Площадь треугольника равна: ", square)
        time.sleep(3)
    except ValueError:
        print("Вы ввели не целое число")