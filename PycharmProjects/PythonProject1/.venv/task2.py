# Зчитуєм дані від користувача та перевіряємо
while True:
    try:
        a = int(input("Введіть ваше трицифрове число"))
        break
    except ValueError:
        print("Ви не ввели число")

per = a // 100
print("перша цифра вашого числа", per)
ost = a % 10
print("остання цифра вашого числа", ost)
if per == ost:
    print("число",a, "є паліндромом")
else:
    print("число",a,"не є паліндромом")


