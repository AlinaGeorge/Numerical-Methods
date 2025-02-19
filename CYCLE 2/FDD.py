def f(x):
    return x**3+2*x**2-5*x+7

h=float(input("Enter the step size:"))
x1=int(input("Enter the point:"))
FDD=(f(x1+h)-f(x1))/h
print("Derivative found using Forward divided difference is:",FDD)

