def  CheckNumberRange() :
    try:
        print ("Проверка входа числа в диапазон")
        from_ = int (input("Диапазон от: "))
        to_ = int (input("Диапазон до: "))
        if (from_ > to_):
            from_ = from_ + to_
            to_ = from_ - to_
            from_ = from_ - to_
        variable4 = int (input("Введите число\n"))
        if (variable4>from_)and(variable4<to_):
            print ("Входит")
        else:
            print ("Не входит")
        time.sleep(3)
    except ValueError:
        print("Вы ввели не целое число")