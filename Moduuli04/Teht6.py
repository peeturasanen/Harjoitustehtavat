import random

N = int(input('Anna arvottavien pisteiden määrä: '))
i = 0
osuu = 0
while i <= N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2+y**2) < 1:
        osuu = osuu + 1
    i = i + 1
print(4*osuu/N)