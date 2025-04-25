def BinSearch(A, lb, ub, key):
    if lb <= ub:
        mid = (lb + ub) // 2
        if key == A[mid]:
            return mid  # Return the index if the element is found
        elif key > A[mid]:
            return BinSearch(A, mid + 1, ub, key)  # Make sure to return the result of the recursive call
        else:
            return BinSearch(A, lb, mid - 1, key)  # Make sure to return the result of the recursive call
    else:
        return -1  # Element not found

# Read inputs from the user
n = int(input("Enter the number of elements: "))
A = []
print("Enter the elements one by one:")
for i in range(n):
    a = int(input())
    A.append(a)

# Sort the array before searching
A.sort()

key = int(input("Enter the key to search: "))
bin = BinSearch(A, 0, n - 1, key)

# Output the result
if bin == -1:
    print("Element not found")
else:
    print("Element found at index", bin)
