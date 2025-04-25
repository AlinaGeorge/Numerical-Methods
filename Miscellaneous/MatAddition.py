def Add(mat1,mat2):
    sum=[]
    for i in range(n1):
        rows=[]
        for j in range(m1):
            add=mat1[i][j]+mat2[i][j]
            rows.append(add)
        sum.append(rows)
    return sum


mat1=[]
mat2=[]
print("Enter the number of row and columns for Matrices:")
m1=int(input("Enter the rows of 1st matrix:"))
n1=int(input("Enter the columns 1st matrix:"))
m2=int(input("Enter the rows 2nd matrix:"))
n2=int(input("Enter the columns 2nd matrix:"))
if m1==m2 and n1==n2:
    for i in range(n1):
        rows=[]
        print("Enter the rows of first matrix one by one:")
        for j in range(m1):
            a=int(input()) 
            rows.append(a)
        mat1.append(rows)

    for i in range(n2):
        rows=[]
        print("Enter the rows of second matrix one by one:")
        for j in range(m2):
            a=int(input()) 
            rows.append(a)
        mat2.append(rows)
    print(mat1)
    print(mat2)
    sum=Add(mat1,mat2)
    print(sum)
else:
    print("Addition not poissible")


