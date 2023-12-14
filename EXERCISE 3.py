#defining the function as triangle
def triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

#asks the users to input the length of a side
print("Enter the lengths of the three sides of a triangle:\n")
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

#prints if the sides can or cannot form a triangle
if triangle(a, b, c):
        print("\nthese side lengths can form a triangle.\n")
else:
        print("these side lengths cannot form a triangle.\n")

#prints the type of triangle
if a == b == c:
       print("The three sides is an equilateral triangle.")

elif a == b or b == c or a == c:
       print("The three sides is an isosceles triangle.")
else:
       print("The three sides is a scalene triangle.")
       



