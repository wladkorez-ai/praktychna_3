num = int(input("Введіть число від 1 до 100: "))

if num < 1 or num > 100:
     print("Помилка: число повинно буди в діапазоні 1-100")
else:
    if num % 2 == 0:
         print("Ділиться на  2")
    else:
        print("Не ділиться на 2")
    if num % 3 == 0:
        print("Ділиться на 3 ")
    else:
        print("Не ділиться на 3")
    if num % 7 == 0:
        print("Ділиться на 7")
    else:
        print("Не ділиться на 7")

