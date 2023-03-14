
#String Manipulation
"""x= "Good Morning Vietnam!"
print(x.upper())
print(x.lower())
print(x.isupper())
print(x.upper().islower())
print(len(x+x))
print(x[0]+x[4]+x[1])
print(x.replace("Good","Shit ass"))
print(x.replace("Good","shit ass"))
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello:"+name+"("+age+")")

y="Good Afternoon"
print(y.capitalize())
print(y.center(2))
print(y.index("oo"))"""
#C:\Users\USER\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pip.

#Number Manipulation
"""print(3+4*3-2/5)
print(10%3)             #Mod Operation
number = 100
str(number)             #String conversio 
abs(-4)
pow(2,3)                #2^3
print(max(1,2,3,4,5,6))"""

#List Manipulation
"""Scale = ["Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Rèaumur", "Rømer"]
print(Scale[2:])
print(Scale[2:4])
print(Scale[-2])
Scale[0] = "Kelcius"

Scale_1 = ["Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Rèaumur", "Rømer"]
Scale_2 = ["ng", "mg", "g", "kg", "ton"]

print(Scale_1)
Scale_1.extend(Scale_2)
print(print('12'))
print(Scale_1)
print(Scale_2.append("dg"))  #cant print list
Scale_1.insert(0,"Kha")
Scale_1.pop()
New_Scale = Scale_1
ultra_list=[Scale_1, Scale_2, Scale, New_Scale]
print(New_Scale)
print(ultra_list)"""

#Tupel Manipulation  ###Tupels are immutable
"""x=3
y=2
coordinate = (x, y)
x=4
print(coordinate)"""

#Functions and if, else, return statement: refer to Temperature_converter.py

#Library
Month_converter = {
"Jan" : "January",
"Feb" : "February",
"Mar": "March",
"Apr": "April",
"May": "May",
"Jun": "June",
"Jul":"July",
"Aug":"August",
"Sep":"September",
"Oct":"october",
"Nov":"November",
"Dec":"December",
}     
#x = input("Enter first three letters of the month: ")
#print(Month_converter.get(x, "Incorrect Input"))
print (Month_converter.__len__())
#While loop
"""i=5
while -1000<=i<=1000:
    if i%2 ==1 :
        i=(i-5)*3
    else: i= (i+2)/2+4

    print(i)
"""
#import getpass
#key_word = getpass.getpass("Enter Keyword here: ")
"""
import os

key_word = input("Enter Keyword here: ")

os.system("cls")

guess_word = input("Make a guess :3 : ")
guess_count = 0
while key_word != guess_word and guess_count <3:
    guess_count += 1
    guess_word = input("Guess again: ")
if guess_count == 3:
    print("You lost")
else:
    print("You won")"""


