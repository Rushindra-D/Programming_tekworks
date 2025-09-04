def Armstrong1toN(n):
    for num in range(1, n + 1):
        sum = 0
        temp = num
        digits = len(str(num))

        while temp > 0:
            digit = temp % 10
            sum += digit ** digits
            temp //= 10

        if num == sum:
            print(num)
n = int(input("Enter the value of n: "))
print(Armstrong1toN(n))
