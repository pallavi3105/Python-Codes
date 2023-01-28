print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")
a=31
print (a)
print(type(a))
b=31
c=a+b;
print(c)
print("b is greater")
c += 3
print(c)

#comparison operator
d=(a>c)
print(d)
print(d)

#boolean operatorp
bool1=True
bool2=False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 and bool2 is",(bool1 or bool2))
print("The value of bool1 and bool2 is",(not bool2))

#Typecasting
aa=111
aa=str(aa)
print(aa+ "pallavi1")

#input function....by default takes input as a string1
a=input("Enter name:")
a=int(a)
print(type(a))

#practice set
#1
a=input("Enter value of a:")
b=input("Enter value of b:")
print("Addition of a and b is:", a+b)


a=12
b=32
print("The remainder of a and b after dividing it is", a%b)

#problem 5
a=input("Enter value of a:")
b=input("Enter value of b:")
a=int(a)
b=int(b)
avj=print(a+b/2)

#String slice...(gives index letter of string)
greeting="Good morning"
name="Pallavi"
print(greeting + name)
print(name[0])

# name[3]="l"......does not work

print(name[0:5])
print(name[:6]) #is ame as name[0:4]
# negative indexes
print(name[-1])

# slicing with skip value
print(name[1:3:6])

# String function
story="Future software engineer pallavi akhade"
print("The length of string:",len(story))
print("The end string of string:",story.endswith("akhade"))
print("The countof letter a in whole string:",story.count("a"))
print("The capatalizing of  string:",story.capitalize())
print("The particular find string:",story.find("pallavi"))
print("The replace of string:",story.replace("pallavi","THE PALLAVI AKHADE"))

# escape character\n\t,\single quote,\\backslash
story="Pallavi is a good student.\n and a good person"
print(story)

# practice set of string
# problem 1
name=input("Enter name:")
greeting="Good afternoon"
print(name + greeting)

# problem 2
letter='''Dear <|name|>,
you are selected!

date:<|date|>
'''

name=input("Enter name:\n")
date=input("Enter date:\n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)

# program to print double places 
st="This is a string with double     spaces" #if no double places then it print -1
doublespaces=st.find("  ")
print(doublespaces)

#problem4
letter="Dear pallavi,\n\t You ara a 'good student'.\nThanks!"
print(letter)