"""Name and age of the person form input & display on the console using format specifier"""

Name="Krushik"
age=23
print(Name,age)
print("Name:",Name,"age:",age)
a=20
b=1.5
city="mandya"
print("%d and %f and %s"%(a,b,city))

"""take a name and age of the person from input and display on the console using f-string"""

a="krushik"
b=23
c="mandya"
print(f"name is {a}")
print(f"age is {b}")
print(f"address is {c}")

"""take name & age  of the person from input & display on the console using format method."""
#name indexes:
txt1 = "my name is {fname},i'm {age}".format(fname="krushik",age=23)
#number indexes:
txt2="my name is {0} i'm {1}".format("krushik",23)
#empty place:
txt3 ="my name is {},i'm {}".format("krushik",23)
print(txt1)
print(txt2)
print(txt3)
# note : permits you to try and do variable substitutions and data formatting

"""take whole number,floating point numbers,string boolean data, cheek each of those data type"""

# integer type: note:(whole number)
print(int(143.14))
print(int("23"))
print(int(True))                 # note:(a whole number, positive or negative, without decimal, of unlimited length)
print(int(False))
print(int(14.20))
x="1420"
print(type(x))
number=int('-20\n')
print(number)

#float type: nate:(number with decimal point)
print(float(20))
print(float(True))
print(float(False))               # note:(convert real number or integer into floating point number)
print(float("14"))
first_number=14.20
print(type(first_number))
print(first_number)

#string type: note: (alphnumaric)
print(str(1))
print(str(14.20))
print(str(1+2j))                   # note:(a collection of alphabets, words or other characters)
first_number=str(14.20)
print(type(first_number))
print(first_number)

#boolean type: note:(true,false)
a= True
print(type(a))
b=False
print(type(b))
c=(1==3)                          # note:(used to represent the true value of an expression)
print(type(c))
a=1.143
print(bool(a))

"""take imput string & extract some part of the string"""
city+"mandya"
print(city[0:4])
print(city[2])
print(city[-2])
print(city[1:3:5])
print(city[: :-3])




      


