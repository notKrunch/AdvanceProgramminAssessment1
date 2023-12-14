# Given array
a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find the indices of even numbers
evenindices = [index for index, value in enumerate(a) if value % 2 == 0]
print("Indices of even numbers:", evenindices)

# Sort the array
sortedarray = sorted(a)
print("Sorted array:", sortedarray)

# Slice elements from index 3 to the end of the array
slice1 = a[3:]
print("Slice from index 3 to the end:", slice1)

# Slice elements from index 0 to index 4
slice2 = a[0:5]
print("Slice from index 0 to index 4:", slice2)

# Print [32, 15, 67] using negative slicing
negativeslice = a[-5:-2]
print("Negative slicing to get [32, 15, 67]:", negativeslice)
