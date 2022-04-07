# Dictionary: Key-Value pairs, unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

value = mydict["name"]
print(value)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

mydict["email"] = "max@xyz.com" #Adds a value to dictionary 
print(mydict)

mydict.pop("age")
print(mydict)

try:
    print(mydict["lastname]"])
except:
    print("Error")