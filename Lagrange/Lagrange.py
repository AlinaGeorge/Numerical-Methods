import math

def lagrange(x, y, n, p):
    sol = 0.0
    for i in range(n):
        num = 1.0
        den = 1.0
        for j in range(n):
            if i != j:
                num *= (p - x[j])
                den *= (x[i] - x[j])  # Prevents division by zero
        sol += (num / den) * y[i]
    print("The value of f(x) at point", p, "is:", sol)

# Input section
n = int(input("Enter the number of values: "))
x = []
for i in range(n):
    x_val = float(input(f"Enter x[{i}]: "))
    x.append(x_val)

y = []
for i in range(n):
    y_val = float(input(f"Enter y[{i}]: "))
    y.append(y_val)

p = float(input("Enter the point to evaluate: "))

# Function call
lagrange(x, y, n, p)
