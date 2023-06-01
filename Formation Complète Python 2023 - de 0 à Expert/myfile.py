""" for i in range(10):
    print(i)
    if i == 5 :
        print(f"i est égale à {i} le programme va s'interumpre !")
        break

i=0
while i < 10 :
    print(i)
    i+=1

i = 0
z = 0
while i < 20 :
    j =  i
    while j < 20 :
        z = z + j
        j = j + 1
        print(i, j, z)
    i = i + 5
print(i, j, z)

sentence = "In Diesem Satz zahlen wir Sechsundvierzig Buchstaben"
num = len(sentence) #sentence length with spaces
j=sentence.count(" ") #sentence length without spaces
print(f"Der Satz hat {num} mit Leerzeichen und {num-j} ohne Leerzeichen")

i = 0
j=0
while i < num :
    if sentence[i]==" " :
        j+=1
    i+=1
print(f"Der Satz hat {num} mit Leerzeichen und {num-j} ohne Leerzeichen")

i = 0  # the counter
for i in range(1, 100):
    divisor_of_3 = i % 3
    divisor_of_5 = i % 5
    if divisor_of_3 == 0 and divisor_of_5 != 0:
        print("Fizz")
    elif divisor_of_3 != 0 and divisor_of_5 == 0:
        print("Buzz")
    elif divisor_of_3 == 0 and divisor_of_5 == 0:
        print("Fizzbuzz")
    else:
        print(i)

auslastung = True
blockiert =  True
angemietet = False

if auslastung and blockiert and angemietet :
    print("Parkhaus gesperrt")
elif auslastung and blockiert and not angemietet :
    print("Parkhaus gesperrt")
elif auslastung and not blockiert and angemietet :
    print("Parkhaus gesperrt")
elif not auslastung and blockiert and angemietet :
    print("Parkhaus gesperrt")
elif not auslastung and blockiert and not angemietet :
    print("Parkhaus gesperrt")
elif not auslastung and not blockiert and angemietet:
    print("Parkhaus gesperrt")
elif auslastung and not blockiert and not angemietet:
    print("Parkhaus belegt")
elif not auslastung and not blockiert and not angemietet:
    print("Parkhaus frei")
else:
    print("Tchao !!!")

value_1 = all([auslastung, blockiert, angemietet])
value_2 = any([auslastung, blockiert, angemietet])
print(value_1)
print(value_2)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [i for i in list if i%2==0]
print(new_list)

lotto = [3, 7, 46, 21, 23, 2]
#if is
print(lotto[0])

for i in range (1, 11):
    print(f"user_{i}")

mot = "python"
revers = reversed(mot)
print(list(revers))

for letter in list(revers):
    print (letter)

number = []
for i in range(100) :
    number.append(i**2)
    print(number)

mot = "Python"
for i in (mot):
    j = mot.index(i)
    print(j)

number = 7
for i in range(11) :
    print(f"{i} x {number} = {i*number}") """




""" my_list = ["User_01", "User_02", "User_03", "User_06", "User_04", "User_05", "User_06"]
print(my_list[0:-2:2])

print(my_list.index("User_01"))

print(my_list.count("User_06"))

print(sorted(my_list))

my_list.reverse()
print(my_list)

my_list.reverse()
element = my_list.pop(-1)
print(my_list)
print(element)

my_list.clear()
print(my_list)

my_list = ["User_01", "User_02", "User_03", "User_06", "User_04", "User_05", "User_06"]
new_list = "-".join(my_list)
print(new_list)

new_list = new_list.split("-")
print(new_list) """



answer = "o"
pwd_to_short = "your password ist to short "

while answer in {"o", "O"}:
    pwd = input("Enter a password (min 8 characters): ")
    if len(pwd) == 0:
            convert_to_upper = pwd_to_short.upper()
            print(convert_to_upper)
            answer = input("Do you want to continue ?")
    elif len(pwd) < 8:
            convert_first_letter_to_upper = pwd_to_short.capitalize()
            print(convert_first_letter_to_upper)
            answer = input("Do you want to continue ?")
    elif pwd.isdigit() == True:
            print("Your password contains only numbers")
            answer = input("Do you want to continue ?")
    elif len(pwd) >=8 and pwd.isdigit() == False:
        if pwd == "Cyrille0":
            print("registration successful")
            break
        else:
            print("The password is incorrect")
            answer = input("Do you want to continue ?")

if answer not in ["o", "O"]:
    print("registration failed")

