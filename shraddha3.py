from unittest import result


name="pallavi Akhade"

print(name.upper())
print(name.lower())
print(name.find('pallavi'))
print(name.replace("Akhade","Pallavi"))

print('pallavi' in name)

i=5
i=i + 2

i += 2
i -= 2
i *= 2
print(i)

result= 2+3*5
print(result)

#logical operators  AND OR NOT
print(2>3 or 2<3)
print(2>3 and 2<3)
print(not 2>3)

#if else statements
age= 20

if (age >=18):
    print("Eligible")
    print("you can vote")
    
elif( age<18 and age>3):
    print("You are in school")
else:
    print("You are not eligible")
