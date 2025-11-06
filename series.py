def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num - 2)
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")
