#Arithmetic Operator:
a = 10
b  = 5
print("Addition:",a+b)
print("subraction:", a-b)
print("multiplication:",a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("modulus:", a%b)
print("expontential:", a**b)
print(" ")

#Assignment Operator:
a = 10
a += 3
print("Assignment Addition:",a)
a -= 3
print("Assignment Subraction:",a)
a *= 4
print("Assignment Multiplication:",a)
a /= 3
print("Assignment Division:",a)
a //= 3
print("Assignment Floor Division:",a)
a %= 4
print("Assignment modulus:", a)
a **= 2
print("Assignment expontential:",a)
print(" ")

#Relational Operator:
a = 10
b = 29
print("Less than operator:",a < b)
print("Greater than operator:",a > b)
print("Less than or equal:", a <= b)
print("Greater than or equal:",a >= b)
print("Equal to :", a == b)
print("Not Equal to:", a != b)
print(" ")

#Logical Operator:
a = 20
b = 30
c = 29
d = 89
print("And Operator:",a < b and d >= c)
print("Or Operator:",a >= b or b//20)
print("Not operator:",a == b ^ b != c)
print(" ")

#Bitwise Operator:
a = 15
b = 65
c = 39
d = 29
print("Bitwise and:",a & b)
print("Bitwise or:",c | d)
print("Left shift:",c << 4)
print("Right shift:",d >> 1)
print("xor:", a ^ d)
print(" ")

#Membership Operator:
a = [10, 20,30]
print("in operator:", 10 in a)
print("not in operator:", 40 in a)
print(" ")

#Identity Operator:
a = 94
b = 32
print("is operator:",a is b)
print("not is operator:", a is not b)
print("")
