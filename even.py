numbers=[int(x)for x in input("Enter numbers separated by space:").split()]
result=[x for x in numbers if x%2!=0]
print("List after removing even numbers:",result)
