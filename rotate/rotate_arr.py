nums1 = []
size = input("Enter size of the array: ")
size = int(size)
for i in range(size):
    inp = input(f"Enter value {i+1}: ")
    nums1.append(int(inp))

print(f"Final array: {nums1}")
rot = input("Enter the rotating value (positive value taken): ") #rotating value is non negative integer
rot = abs(int(rot))

for i in range(rot):
    while i < rot:
        nums1_pop = nums1.pop()
        nums1.insert(0, nums1_pop)
        print(f"Inserted number :{nums1_pop}")
        break
    
print(f"Rotated Array: {nums1}")
        