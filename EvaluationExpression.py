def EvaluationExpression():
    try:
        sum = (input("Введите выражение: \n").split("+"))
        sum1 = int(sum[0]) + int(sum[1])
        print(sum1)
    except ValueError:
        print("Вы ввели не целое число")
