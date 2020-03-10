def get_number():
    return int(input("Gebe eine Nummer an: "))
def oddoreven(int):
    if num % 2 == 0:
        return print("Your number is even")
    else:
        return print("Your number is odd")

num = get_number()
oddoreven(num)
