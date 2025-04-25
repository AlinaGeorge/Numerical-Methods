def f(x):
    return x**2  # Example function

def trapezoidal(a, b, n):
    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):
        total += 2 * f(a + i * h)

    total *= h / 2
    return total

# Input section
a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
n = int(input("Enter the number of intervals (n): "))

# Compute and print result
result = trapezoidal(a, b, n)
print("The integral is:", result)
