numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes = []
for i in numbers:
    if i==1:
        continue
    is_not_prime = False
    for j in range(2,i):
        if i % j ==0:
            #print(f' i={i} j={j}')
            not_primes.append(i)
            is_not_prime = True
            break
    if not is_not_prime:
        primes.append(i)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
