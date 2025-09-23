s = input("Enter astring:")
if len(s) > 1:
    new_s = s[-1] + s[1:-1] + s[0]
else:
    new_s = s
print("string after swapping:", new_s)

