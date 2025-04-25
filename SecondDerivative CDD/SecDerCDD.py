import math 
def f(x):
    return math.sin(x)

h=0.05
x1=math.pi/4
CDD=(f(x1+h)+f(x1-h)-(2*f(x1)))/(h**2)

print("Second Derivative found using Central divided difference is:",CDD)
