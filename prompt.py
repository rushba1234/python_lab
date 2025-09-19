num = input("Enter integers separated by space: ").split()
result=[int(n) if int(n)<=100 else "over" for n in num]
print(result)


