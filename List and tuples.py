# creating a list using[]
a=[1,2,3,9,5]
print(a[3])

#access using index
a.sort()
print(a)
a.reverse()
print(a)
a.append(21)
print(a)
a.insert(3,8)
print(a)
a.pop(2)  #index 3 get popped
print(a)
a.remove(21)
print(a)


#values from tuple does not change
t=(1,2,3,4)
t1=(1) #wrong way to declare tuple
t1=(1,)  #tuple with single element
print(t1)

# printing the element of the tuple
# print(t[0])

# methods of tuple

t=(1,2,3,2,3,2,5)
print(t.count(2))
print(t.index(2))

#program 1..program to enter names of fruits entered by user
f1=input("Enter name 1:")
f2=input("Enter name 2:")
f3=input("Enter name 3:")
f4=input("Enter name 4:")
f5=input("Enter name 5:")
f6=input("Enter name 5:")
f7=input("Enter name 7:")

myFruitList=(f1,f2,f3,f4,f5,f6,f7)
print(myFruitList)

#program2...
f1=int(input("Enter name 1:"))
f2=int(input("Enter name 2:"))
f3=int(input("Enter name 3:"))
f4=int(input("Enter name 4:"))
f5=int(input("Enter name 5:"))
f6=int(input("Enter name 6:"))

myList=[f1,f2,f3,f4,f5,f6]
myList.sort()
print(myList)

#program3...tuple change test
a=(2,4,3,1,5)
print(a[0]+a[1]+a[2])
print(sum())