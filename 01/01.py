# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day_number = int(input("Введите номер дня недели: "))
if 0 < day_number < 8:
    if day_number > 5:
        print("yes")
    else:
        print("no")
else:
    print("Введите корректный номер дня недели")
