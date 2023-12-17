def sum_nums(a,b):
    result = 0
    try:
        result = a + b
    except:
        print("Функция сложения работает только с числами.")
    finally:
        return result


def sub_nums(num1,num2):
    result = 0
    try:
        result =float(num1) - float(num2)
    except:
        print("Функция вычитания работает только с числами")
    finally:
        return result

def multiply_nums(num1,num2):
    result = 0
    try:
        result =float(num1) *  float(num2)
    except:
        print("Функция умножения работает только с числами.")
    finally:
        return result


def divide_nums(num1, num2):
    result = 0
    try:
        result = float(num1) / float(num2)
    except ZeroDivisionError:
        print("Нельзя делить на ноль.")
    except:
        print("Функция деления работает только с числами.")
    finally:
        return result

print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
choice = input('Введите номер действия: ')
if choice == "1":
    num1 = int(input())
    num2 = int(input())
    print(sum_nums(num1,num2))

elif choice == "2":
    num1 = int(input())
    num2 = int(input())
    print(sub_nums(num1,num2))

elif choice == "3":
    num1 = int(input())
    num2 = int(input())
    print(multiply_nums(num1,num2))

elif choice == "4":
    num1 = int(input())
    num2 = int(input())
    print(divide_nums(num1,num2))
