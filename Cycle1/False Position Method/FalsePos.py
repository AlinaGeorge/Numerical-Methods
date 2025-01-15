def f(x):
    return x**3-4*x-9

def FindInterval():
    i=0
    """if f(i)==0:
        print("The root is:",i)
        return i"""
    #else:
    while f(i)*f(i+1)>=0:
        if f(i)==0:
            print("The root is:",i)
            return i
        else:
            i=i+1
    return i
    
a=FindInterval()
b=a+1 
print("The interval is [",a,",",b,"]")

def FalsePos(a,b, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        x=(a*f(b)-b*f(a))/(f(b)-f(a))
        #x = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(x)) < tol:
            print(f"Root found: x = {x} after {iter_count+1} iterations")
            return x
        
        if f(x)==0:
            print("The root is:",x)
            return x
        elif f(a)*f(x)<0:
            b=x
        else:
            a=x
        iter_count += 1
    print(f"Maximum iterations reached. Approximate root: x = {x}")
    return x
   
root = FalsePos(a, b)
print("The root is approximately:", root)
