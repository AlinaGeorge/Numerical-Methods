def f(x):
    return 2/(1+x**3)

a=int(input("Enter the lower interval:"))
b=int(input("Enter the upper interval:"))
n=int(input("Enter the n:"))
h=(b-a)/n

sumodd=0
sumeven=0

for i in range (1,n):
    if(i%2==0):
        sumeven=sumeven+f(a+i*h)
    else:
        sumodd=sumodd+f(a+i*h)
    
simp=(h/3)*(f(a)+f(b)+4*sumodd+2*sumeven)
print("Integral using Simpsons method:",simp)
