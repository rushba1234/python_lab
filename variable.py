def add_numbers(*args):
    return sum(args)
numbers = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in numbers.split()]
print("Sum =", add_numbers(*nums))


