def seidel(a, x ,b):      
    n = len(a)                   
    for j in range(0, n):        
        d = b[j]                  
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
             
        x[j] = d / a[j][j]
            
    return x    
             
n = 3                             
a = []                            
b = []        
                    
x = [0, 0, 0]

#Enter the matrix in diagonally dominant form                        
a = [[5, 1, 3],[1, 10, 9],[2,-7,-10]]

b = [14,7,-17]
print(x)

for i in range(0, 15):            
    x = seidel(a, x, b)
    
    print(x)  
