def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primesupton(n):
    primes = []
    for number in range(2, n + 1):
        if prime(number):
            primes.append(number)
    return primes
n = 30
print(primesupton(n))
