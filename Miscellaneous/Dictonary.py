#creating dictionary
dict1={"A1":'a',"A2":'b',"A3":'c',"A4":'d'}
print(dict1)

#accesing value using key
key=input("Enter the key to access:")
a=dict1[key]
print(a)

#to insert a key value pair
key=input("Enter the key to insert:")
val=input("Enter the value to insert:")
dict1[key] = val
print(dict1)

#to remove a key-value pair
key=input("Enter the key to delete:")
del dict1[key]
print(dict1)

#to pop out an element
pos=input("Enter the key to pop:")
popp= dict1.pop(pos)
print(dict1)
print("The popped element is:",popp)

#to get all the elements
keys=dict1.keys()
print("Gettin all the element",keys)
