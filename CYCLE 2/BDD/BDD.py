import math
def f(x):
    return math.exp(x)

h=float(input("Enter the step size:"))
x1=int(input("Enter the point:"))

BDD=(f(x1)-f(x1-h))/h
print("Derivative found using backward divided difference is:",BDD)
