start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for n in range(start, end + 1):
    if int(n**0.5)**2==n:
        if all(int(d) % 2 == 0 for d in str(n)):
                print(n)
