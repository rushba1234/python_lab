terms = int(input("Enter number of terms:"))
powers = list(map(lambda x:2 ** x,range(terms)))
print("The power of 2 are:")
for i in range(terms):
    print(f"2^{i} = {powers[i]}")
