import math
def is_strong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += math.factorial(digit)
        temp //= 10
    return sum == num
print(is_strong(145))
