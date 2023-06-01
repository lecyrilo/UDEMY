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
