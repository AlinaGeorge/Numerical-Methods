import math

def forward(x, y, n, p):
    a = []
    a.append(y)  # First row is just y

    # Building the difference table
    for i in range(n - 1):
        b = []
        for j in range(n - i - 1):
            b.append(a[i][j + 1] - a[i][j])
        a.append(b)

    # Calculating the value of u
    h = x[1] - x[0]  # Assuming uniform spacing
    u = (p - x[0]) / h  # u = (x - x0)/h

    # Newton forward interpolation formula
    sol = a[0][0]
    u_term = 1
    for i in range(1, n):
        u_term *= (u - (i - 1))
        sol += (u_term * a[i][0]) / math.factorial(i)

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
forward(x, y, n, p)
