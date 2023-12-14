# 10 different numbers
numbers = [696969, 69, 6, 9 , 96, 12, 4, 25, 48 , 0]

#the list using a for loop
print("List:")
for num in numbers:
    print(num, end=" ")

print("\n")

#highest and lowest value
print("\nHighest Value:", max(numbers))
print("Lowest Value:", min(numbers))

#sort in ascending order
numbers.sort()
print("\nAscending Order:", numbers)

#sort in descending order
numbers.sort(reverse=True)
print("Descending Order:", numbers)

#add two numbers
numbers.append(13)
numbers.append(27)

#print the list after adding two numbers
print("\nList after adding 2 numbers :", numbers)
