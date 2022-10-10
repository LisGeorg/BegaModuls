def RaisingNumToPower():
	try:
		print ("Возведение числа в степень")
		variable6 = int (input("Введите число: "))
		degree = int (input("Введите степень: "))
		result = variable6**degree
		print (result)
		time.sleep(3)
	except ValueError:
		print("Вы ввели не целое число")
		time.sleep(3)
