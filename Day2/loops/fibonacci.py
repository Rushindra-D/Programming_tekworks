def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


n = int(input("Enter number of terms: "))
fibonacci(n)
