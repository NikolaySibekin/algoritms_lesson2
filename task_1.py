# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

print("Программа завершится, если ввести символ '0'")
while True:
        s = input("Введите знак операции (+,-,*,/): ")
        if s == '0':
            break
        if s in ('+', '-', '*', '/'):
                x = float(input("x = "))
                y = float(input("y = "))
                if s == '+':
                        print(f"x + y = {x + y:.2f}")
                elif s == '-':
                        print(f"x - y = {x - y:.2f}")
                elif s == '*':
                        print(f"x * y = {x * y:.2f}")
                elif s == '/':
                        if y != 0:
                                print(f"x / y = {x / y:.2f}")
                        else:
                                print("Нельзя делить на ноль!!!")
        else:
                print("Неверный знак операции!")
