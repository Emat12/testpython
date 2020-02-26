
#Numeral literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
print("*********************************END OF NUMERAL LITERAL****************************")

#String literals
strings="This is Pythin"
char="C"
multiline_str="""This is the multiline string with more than one line code"""
unicode= u"\u00dcnic\u00f6de"
raw_str=r"raw \n string"

print( strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
print("********************************END OF STRING LITERAL ******************************")

#Boolean literals
x=(1==True)
y=(1==False)

a=True+4
b=False +10

print("x is",x)
print("y is", y)
print(a)
print(b)
print("********************************END OF BOOLEAN LITERAL ******************************")

#Special literals i.e None , used to specify to that field that is not created
drink="Available"
food=None

def menu(x):
    if x==drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)
print("********************************END OF SPECIAL LITERAL ******************")

#Literal Collections,i.e list, tuple,dict ,set
fruits=["apple","mango","orange"] #list
numbers=(1,2,3) #tuple
alphabets={'a':'apple','b':'ball','c':'cat'} #dictionary
vowels={'a','e','i','o','u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

        


      

