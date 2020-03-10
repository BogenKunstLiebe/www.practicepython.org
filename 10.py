import random
a = random.sample(range(1,50),10)
b = random.sample(range(1,50),10)

u = [i for i in a if i in b]
print(u)
