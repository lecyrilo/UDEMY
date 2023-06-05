def addition(a,b):
    answer_1 = "o"
    while answer_1 in {"o", "O"}:
        a= input("Enter a number:")
        b = input("Enter a number:")
        is_number_a = a.isnumeric()
        is_number_b = b.isnumeric()
        if is_number_a == True and is_number_b == True:
            print(int(a) + int(b))
            break
        else:
            print("You must enter numbers")
            answer_1 = input("Do you want to continue ?")

    if answer_1 not in {"o", "O"}:
        print("We are sorry, but we are unable to perform this operation")
    else:
        print("Operation successful")

number_1= input("Enter a number:")
number_2 = input("Enter a number:")
addition(number_1, number_2)

""" answer_2 = "o"
while answer_2 in {"o", "O"}:
    number_1= input("Enter a number:")
    number_2 = input("Enter a number:")
    addition(number_1,number_2)
    answer_2 = input("would you like to perform another operation?")
print("Thank you for visiting us !") """
