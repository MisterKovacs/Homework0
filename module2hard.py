from random import randint
n = randint(3, 20)
print(f'Первый камень - {n}')
for i in range(1, 21):
    for x in range(1, 21):
        if n % (i + x) == 0 and i < x:
            print(i, x, '/', end=' ')





