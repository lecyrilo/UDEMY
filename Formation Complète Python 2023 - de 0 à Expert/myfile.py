""" for i in range(10):
    print(i)
    if i == 5 :
        print(f"i est égale à {i} le programme va s'interumpre !")
        break """

""" i=0
while i < 10 :
    print(i)
    i+=1 """

""" i = 0
z = 0
while i < 20 :
    j =  i
    while j < 20 :
        z = z + j
        j = j + 1
        print(i, j, z)
    i = i + 5
print(i, j, z) """

""" sentence = "In Diesem Satz zahlen wir Sechsundvierzig Buchstaben"
num = len(sentence) #sentence length with spaces
j=sentence.count(" ") #sentence length without spaces
print(f"Der Satz hat {num} mit Leerzeichen und {num-j} ohne Leerzeichen") """

""" i = 0
j=0
while i < num :
    if sentence[i]==" " :
        j+=1
    i+=1
print(f"Der Satz hat {num} mit Leerzeichen und {num-j} ohne Leerzeichen") """

""" i = 0  # the counter
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
        print(i) """

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

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [i for i in list if i%2==0]
print(new_list)

lotto = [3, 7, 46, 21, 23, 2]
print(lotto[0])

for i in range (1, 11):
    print(f"utilisateur_{i}")