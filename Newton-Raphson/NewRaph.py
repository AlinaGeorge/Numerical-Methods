import sympy as sp

def f(x):
    return x**3 +2*x - 2

def FindInterval():
    i = 0
    while f(i) * f(i + 1) >= 0:
        if f(i) == 0:
            print("The root is:", i)
            return i
        else:
            i += 1
    return i

a = FindInterval()
b = a + 1 
print("The interval is [", a, ",", b, "]")

if abs(f(a))>=abs(f(b)):
    x=b
else:
    x=a

def deri(x):
  x_symb= sp.symbols('x')
  f_expr = x_symb**3 + 2*x_symb - 2
  derivative = sp.diff(f_expr, x_symb)
  derVal=derivative.subs(x_symb,x)
  #print(derVal)
  return derVal

tolerance = 1e-6 

def NewRaph(x):
  prev_x=x
  while True:    
    x=prev_x-float((f(x)/deri(x)))
    if abs(prev_x-x)<tolerance:
      break
    prev_x=x
    print(x)
  return x

NewRaph(x)
