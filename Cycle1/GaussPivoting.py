def gauss_elimination_pivoting(a, b):
    n = len(a)

    # Augment matrix A with column B
    for i in range(n):
        a[i].append(b[i])

    # Forward elimination with partial pivoting
    for i in range(n):
        # Partial pivoting: find the max row
        max_row = i
        for k in range(i+1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k
        # Swap rows
        a[i], a[max_row] = a[max_row], a[i]

        # Eliminate entries below pivot
        for k in range(i+1, n):
            factor = a[k][i] / a[i][i]
            for j in range(i, n+1):
                a[k][j] -= factor * a[i][j]

    # Back substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = a[i][-1]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]

    return [round(val) for val in x]  # Rounded output

# Example usage
A = [[2, -7, -10],
     [5, 1, 3],
     [ 1, 10,9]]
B = [-17, 14, 7]

sol = gauss_elimination_pivoting(A, B)
print("Solution:", sol)
