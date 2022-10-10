import math
import time
import CalcOfTheAreaRectangle
import Menu
import TriangleExistenceTest
import CalcOfHypoValues
import CheckNumberRange
import CalcAreaTriangleHeightBase
import RaisingNumToPower
import CheckMultipNum
import FindPa
import EvaluationExpression
import pallindrom
import Count2
import findMin
import sumnum



print("Добро пожаловать!")
z = 1
while (z == 1):
    print("\nСписок программ:\n")
    print("1.Вычисление площади прямоугольника")
    print("2.Проверка существования треугольника")
    print("3.Вычисление значения гипотенузы через катеты")
    print("4.Проверка входа числа в диапазон")
    print("5.Вычисление площади треугольника через высоту и основание")
    print("6.Возведение числа в степень")
    print("7.Проверка кратности числа")
    print("8.Поиска 'ра'")
    print("9.Сложение")
    print("10.Проверка на паллиндрому")
    print("11.Подсчет количества двоек")
    print("12.Нахождение наименьшего")
    print("13.Сумма введенных чисел")
    print("14.Меню")
    number = int (input ("Введите номер нужной программы:"))
    if (number == 1):
        CalcOfTheAreaRectangle.CalcOfTheAreaRectangle()
    if (number == 2):
        TriangleExistenceTest.TriangleExistenceTest()
    if (number == 3):
        CalcOfHypoValues.CalcOfHypoValues()
    if (number == 4):
        CheckNumberRange.CheckNumberRange()
    if (number == 5):
        CalcAreaTriangleHeightBase.CalcAreaTriangleHeightBase()
    if (number == 6):
        RaisingNumToPower.RaisingNumToPower()
    if (number == 7):
        CheckMultipNum.CheckMultipNum()
    if (number == 8):
        FindPa.FindPa()
    if (number == 9):
        EvaluationExpression.EvaluationExpression()
    if (number == 10):
        pallindrom.pallindrom()
    if (number == 11):
        Count2.Count2()
    if (number == 12):
        findMin.findmin()
    if (number == 13):
        sumnum.sumnum()
    if (number == 14):
        Menu.Menu()
