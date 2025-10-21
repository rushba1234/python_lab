color_list1=input("Enter color for list1:").split()
color_list2=input("Enter color for list2:").split()
result=[color for color in color_list1 if color not in color_list2]
print("colors in list1 not in list2:",result)
