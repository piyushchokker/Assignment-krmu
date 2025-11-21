# Insert element 

# arr = [10, 20, 30, 40, 50]
# print("Original Array:", arr)

# pos = int(input("Enter position: "))
# value = int(input("Enter value to insert: "))

# if pos < 0 or pos > len(arr):
#     print("Invalid position!")
# else: 
#     arr.insert(pos, value)
#     print("Array after insertion:", arr)


# Delete element 

# arr = [10, 20, 30, 40, 50]
# print("Original Array:", arr)

# pos = int(input("Enter position: "))

# if pos < 0 or pos >= len(arr):
#     print("Invalid position!")
# else:
#     deleted = arr.pop(pos)
#     print(f"Deleted element: {deleted}")
#     print("Array after deletion:", arr)


# Search element 

arr = [10, 20, 30, 40, 50]   
print("Array:", arr)

value = int(input("Enter value to search: "))

if value in arr:
    pos = arr.index(value)
    print(f"Element {value} found at position {pos}")
else:
    print(f"Element {value} not found!")

