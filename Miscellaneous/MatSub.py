def Sub(mat1,mat2):
    dif=[]
    for i in range(n1):
        rows=[]
        for j in range(m1):
            dif1=mat1[i][j]-mat2[i][j]
            rows.append(dif1)
        dif.append(rows)
    return dif


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
    dif=Sub(mat1,mat2)
    print(dif)


