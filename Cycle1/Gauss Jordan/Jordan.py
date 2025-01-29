class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.mat=[[0 for i in range(cols)]for j in range(rows)]

    def setMat(self):
        for i in range(self.rows):
            print("Enter the value for row ",i+1)
            for j in range(self.cols):
                val=float(input())
                self.mat[i][j]=val

    def printMat(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.mat[i][j],end="\t")
                
            print()
        print()
    def swap(self,r1,r2):
        for i in range(self.cols):
            temp=self.mat[r1][i]
            self.mat[r1][i]=self.mat[r2][i]
            self.mat[r2][i]=temp
    def reduceMat(self):
        for i in range(self.rows):
            if self.mat[i][i]==0:
                while self.mat[i][i]==0:
                    if i<self.rows-1:
                        swap(i,i+1)
                    else:
                        swap(i,0)
        # making the matrix upper triangular
        for i in range(1,self.rows):
            for j in range(i):
                ratio=self.mat[i][j]/self.mat[j][j]
                for k in range(self.cols):
                    self.mat[i][k]=self.mat[i][k]-(ratio*self.mat[j][k])

        # making the matrix diagonal
        for l in range(self.rows-2,-1,-1):
            for n in range(self.cols-2,l,-1):
                ratio=self.mat[l][n]/self.mat[n][n]
                for m in range(self.cols):
                    self.mat[l][m]=self.mat[l][m]-(ratio*self.mat[n][m])
        # making the matrix into row echelon form
        for i in range(self.rows):
            pivot = self.mat[i][i]
            if pivot != 0:  # Ensure we are not dividing by zero
                for j in range(self.cols):
                    self.mat[i][j] /= pivot
                    
        #solutionSet
        arr=[]
        for i in range(self.rows):
            arr.append(self.mat[i][self.cols-1])
        return arr
r=int(input("Enter the number of rows in the augmented matrix:"))
c=int(input("Enter the number of columns in the augmented matrix:"))
m=Matrix(r,c)
m.setMat()
sol=[]
sol=m.reduceMat()
print(sol)
