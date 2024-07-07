c = float(input("enter your first number:"))
d = float(input("enter your second number:"))

print("enter 1 for 'add' \nenter 2 for 'sub' \nenter 3 for 'mul' \nenter 4 for 'div' ")

enter_number = int(input("choose number: "))

if enter_number == 1:
    print(c+d) 
elif enter_number == 2:
    print(c-d) 
elif enter_number == 3:
    print(c*d) 
elif enter_number == 4:
    print(c//d)
else:
    print("you press the wrong number, Please press the correct number 1:4")
    
    enter_number = int(input("choose number: "))
    if enter_number == 1:
        print(c+d) 
    elif enter_number == 2:
        print(c-d) 
    elif enter_number == 3:
        print(c*d) 
    elif enter_number == 4:
        print(c//d)
                