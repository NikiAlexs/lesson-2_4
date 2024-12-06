#list_ = ['one', 'two', 'three']
#list_2 = [2, 3, 4, 5, 1]
#sum_ = 0
#for i in range(len(list_2)):
#    sum_ += list_2[i]
#print(sum_)
#for i in range(1,11):
#    for j in range(1,11):
#       print(f'{i} x {j} = {i * j}')
#    print(i)

#Домашняя работа по циклу For.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] < 2:
        continue
    is_prime = True
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
print(primes)
print(not_primes)

