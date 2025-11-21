# Queue Insert Enqueue 

# queue = []
# MAX_SIZE = 5

# print("Initial Queue:", queue)

# value = int(input("Enter value to insert in queue: "))

# if len(queue) == MAX_SIZE:
#     print("Queue Overflow!")
# else:
#     queue.append(value)   
#     print("After Insertion:", queue) 


# Queue Delete Dequeue

# queue = [10, 20, 30, 40]   
# print("Current Queue:", queue)

# if not queue:
#     print("Queue Underflow!")
# else:
#     deleted = queue.pop(0)  
#     print(f"Deleted element: {deleted}")
#     print("After Deletion:", queue)


    
# Queue Search Program

queue = [10, 20, 30, 40, 50]
print("Queue:", queue)

value = int(input("Enter value to search: "))

if value in queue:
    pos = queue.index(value)
    print(f"Element {value} found at position {pos}")
else:
    print(f"Element {value} not found in queue!")
