def f(x):
    return x**2-4
def bisection_method(a,b,tol,max_iter):
    if f(a) * f(b) >= 0:
        print("The Bisection method cannot be applied.f(a) and f(b) must have opposite signs.")
        return None    
    iter_count=0
    while (b-a)/2>tol:
        c=(a+b)/2
        if f(c)==0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c      
        iter_count += 1
        if iter_count >= max_iter:
            print("Maximum iterations reached.")
            break    
    return (a + b) / 2
a = 0 
b = 3  
tolerance = 1e-6  
max_iterations = 100  
root = bisection_method(a, b, tolerance, max_iterations)
if root is not None:
    print(f"Root found at: {root}")
