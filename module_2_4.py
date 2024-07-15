numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in numbers:
    if i > 1:
        a = 0
        for j in range(1, i+1):
            if i % j == 0:
                a = a + 1
        if a == 2:
            primes.append(i)
        else:
            not_primes.append(i)
print(primes)
print(not_primes)