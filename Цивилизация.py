# Это тире, возьми его –
import random as r
forest = -1
desert = -1
print("Ты – вождь небольшого племени. В нём есть всего 10 человек")
people = 10
print("Распредели их по местам назначения. Есть следующие места:")
print("Лес. В нём добывается пища ипрочие базовые ресурсы")
print("Пустыня. Здесь можно размышлять для получения технологий")
print("Поселение. Те, кто стоит здесь, обеспечивают защиту")
while forest < 0:
    forest = int(input("Сколько людей ты отправишь в лес?\n"))
    if forest >= people:
        forest = -1
        print("У тебя нет столько людей")
while desert < 0:
    desert = int(input("Сколько людей ты отправишь в пустыню?\n"))
    if desert >= people - forest:
        desert = -1
        print("У тебя нет столько людей")
site = people - forest - desert
print("Остальные люди останутся в поселении")
food = forest * 3
i = 0
while i < forest:
    find_stick = r.randint(1, 3)
    if find_stick == 3:
        print("Один из людей нашёл палку")
    i += 1
