#creation of list
l=int(input("Enter the lenth of array:"))
for i in range(l):
    ele=int(input("Enter the value to insert:"))
    list1.append(ele)



val=int(input("Enter the value to insert:"))
list1=[1,2,3,4,5]
print(list1)

#to access an element
n1=int(input("Enter the position of element to access:"))
a=list1[n1]
print(a)

#to append into the list
n2=int(input("Enter the element to append:"))
list1.append(n2)
print(list1)

#to pop out an element of the list
popp=list1.pop()
print("Popped List:",list1)
print("The last element popped is:",popp)
pos=int(input("Enter the index to pop:"))
popp1=list1.pop(pos)
print(list1)
print("The popped element is:",popp1)

#to insert a value into the list
ind=int(input("Enter the position of element to insert:"))
val=int(input("Enter the value to insert:"))
list1.insert(ind,val)
print(list1)

#to remove an element
val=int(input("Enter the value to remove:"))
list1.remove(val)
print(list1)

#to find length of the list
print("Lenth of the list is: ",len(list1))

#to reverse the list
list1.reverse()
print("Reversed List:",list1)

#to sort the list
list1.sort()
print("Sorted List:",list1)