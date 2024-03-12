#Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon,
#és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot,
#és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót,
#és írja ki a lista elemeit a képernyőre!


import random

random_szamok = []


for i in range(5):
    random_szamok.append(random.randint(1,7))

bekert = int(input("Kérek egy egész számot: "))

talált = False

for szam in random_szamok:
    if szam == bekert:
        talált = True
if talált:
    print(f"A bekért szám benne van a listában! ")
else:
    print(f"A bekért szám nincs benne a listában! ")
print(random_szamok)