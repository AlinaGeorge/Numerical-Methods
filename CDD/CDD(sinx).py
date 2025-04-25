import math 
def f(x):
    return math.sin(x)

h=0.05
x1=math.pi/4
FDD=(f(x1+h)-f(x1-h))/(2*h)

print("Derivative found using Forward divided difference is:",FDD)
