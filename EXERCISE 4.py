#asks the user to enter three numbers
print("Enter three numbers: ")
num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
print("\n")

# if statements to compare the largest numbers among three inputs
if num1 > num2 and num3:
    print(num1, "is the largest number among:", num1,",", num2,",", num3)

elif num2 > num1 and num3:
    print(num2, "is the largest number among:", num1,",", num2,",", num3)

elif num3 > num1 and num2:
    print(num3, "is the largest number among:", num1,",", num2,",", num3)
