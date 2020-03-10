def get_fibonacci(int):
    n1, n2, = 0, 1
    count = 0
    while count < num:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

num = int(input("Anzahl der Komastellen: "))
get_fibonacci(num)
    
