from random import randint

number = randint(1,9)
user = float(input('Gebe eine Nummer zwischen 1 und 9 an: '))


if user < number:
    print("Deine Nummer ist zu klein")
    print("Die gesuchte Nummer war:" )
    print(number)
if user > number:
    print("Deine Nummer ist zu groß")
    print("Die gesuchte Nummer war:")
    print(number)
if user == number:
    print("Du hast gewonnen!")
    print(number)
