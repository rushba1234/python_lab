def calculate_interest(principal, time, is_senior):
    rate = 12 if is_senior else 10
    return (principal * rate * time) / 100

p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
senior = input("Is the customer a senior citizen? (yes/no): ").lower() == "yes"

si = calculate_interest(p, t, senior)
print("Simple Interest =", si)
