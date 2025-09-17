basic_pay=float(input("Enter the basic pay of the employee:"))
HRA=0.10*basic_pay
TA=0.05*basic_pay
salary=basic_pay+HRA+TA
print("basic pay:",basic_pay)
print("HRA(10%):",HRA)
print("TA(5%):",TA)
print("total salary:",salary)
