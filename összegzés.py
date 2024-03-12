#Készíts egy programot,
#amely [1;10] intervallumon generál 5 darab véletlen egész számot,
#és ezeket tárolja el egy listában! A program adja össze a lista elemeit,
#írja ki a képernyőre az összegüket és a lista elemeit!



import random

random_szamok = []


for i in range(5):
    random_szamok.append(random.randint(0,10))

összeg = 0

for szam in random_szamok:
    összeg += szam 

print(összeg, random_szamok)


    
    


