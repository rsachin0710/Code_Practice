#Prompt the user to specify the size of the array, accept that many numbers as input, and reverse the final array.

size = input("Enter the size of the array: ")
try:
    size = int(size)
except ValueError:
    print("Enter an integer value")

arr = []
for i in range(size):
    item = input(f"Enter value {i+1}: ")
    item = int(item)
    if not isinstance(item, int):
        print(f"Enter the value {i+1} again")
    else:
        arr.append(item)

print(f"Final array entered: {arr}")

revarr = []
for i in range(len(arr)-1 ,-1,-1):
    revarr.append(arr[i])

print(f"The reversed array is {revarr}")
