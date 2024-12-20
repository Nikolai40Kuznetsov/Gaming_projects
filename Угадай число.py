import random as r
print("Приветствую!")
number = r.randint(1, 10001)
print("Я загадал число от 1 до 10000. Попробуй его угадать!")
while True:
    check = int(input("Назови число: "))
    if check > number:
        print("Моё число меньше")
    if check < number:
        print("Моё число больше")
    if check == number:
        print("Угадал!")
        break