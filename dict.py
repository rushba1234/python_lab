dict1 = eval(input("Enter first dictionary:"))
dict2 = eval(input("Enter second dictionary:"))
merged={**dict1,**dict2}
print("Merged dictionary:",merged)
