myDict={
    "fast":"In a quick manner",
    "Pallavi":"A coder",
    "marks":[2,3,4],
    "Anotherdict":{"Pallavi":"Hacker"}
}
print(myDict["Anotherdict"]["Pallavi"])
print(myDict["marks"])

print((myDict.keys()))
print(myDict.items())
print(myDict)
updateDict={
    "hii":"pallavi"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("Pallavi"))

# dictionary is unordered,mutable,indexed. can't contain duplicate values....


#SETS...non-repeated values.....
s={"january","february","march","april"}
print(s.remove("april"))