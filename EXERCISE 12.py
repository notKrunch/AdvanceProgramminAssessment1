#import math
import math

#asks the user to choose the shape to calculate
choice = str(input("Choose the shape you want to calculate (Circle, Triangle, Square): ")).lower()

#function to calculate the area and circumference of circle
if choice == "circle":
    radius = float(input("Enter the radius of the circle: "))
    answer = str(input("Enter A/a for area and C/c for circumference: ")).lower()
    if answer == "a":
        areaofcircle = math.pi * radius**2
        print("The area of the circle is: ", areaofcircle)
    elif answer == "c":
        circumofcircle = 2 * math.pi * radius
        print("The circumference of the circle is ", circumofcircle)
    else:
        print("INVALID!")

#function to calculate the area and perimeter of triangle
elif choice == "triangle":
    answer1 = str(input("Enter A/a for area and P/p for perimeter: ")).lower()
    if answer1 == "a":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        areaoftriangle = base * height / 2
        print("The area of the triangle is :", areaoftriangle)
    elif answer1 == "p":
        side = float(input("Enter the side of the triangle: "))
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        perimoftriangle = side + base + height
        print("The perimeter of the triangle is: ", perimoftriangle)
    else:
        print("INVALID!")

#function to calculate the area and perimeter of square
elif choice == "square":
    sideofsq = float(input("Enter the side length of the square: "))
    answer2 = str(input("Enter A/a for area and P/p for perimeter: ")).lower()
    if answer2 == "a":
        areaofsquare = sideofsq**2
        print("The area of the square is: ", areaofsquare)
    elif answer2 == "p":
        perimofsquare = 4 * sideofsq
        print("The perimeter of the square is: ", perimofsquare)
else:
    print("Error!")
    