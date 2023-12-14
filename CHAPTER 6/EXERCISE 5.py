import json

# Create a function to write details to JSON file
def writetojson(studentdetails):
    with open('StudentJson.json', 'w') as jsonfile:
        json.dump(studentdetails, jsonfile)

# Create a function to read and print all the values from JSON file
def readfromjson():
    with open('StudentJson.json', 'r') as jsonfile:
        studentdetails = json.load(jsonfile)
        print("\nDetails of the Student are")
        print(f"\tName: {studentdetails['Name']}")
        print(f"\tID: {studentdetails['ID']}")
        print(f"\tcourse: {studentdetails['course']}")
        coursedetails = studentdetails.get("CourseDetails", {})
        print(f"\tGroup: {coursedetails.get('Group', 'N/A')}")
        print(f"\tYear: {coursedetails.get('Year', 'N/A')}")

# Enter the input for student details
studentname = input("Enter the student name: ")
studentid = input("Enter the student ID: ")
course = input("Enter the course: ")

# Create a dictionary for student details
studentdetails = {
    "Name": studentname,
    "ID": int(studentid),
    "course": course
}

# Write initial details to JSON file
writetojson(studentdetails)

# Add course details to student details dictionary
coursedetails = {
    "Group": "A",
    "Year": 2
}
studentdetails["CourseDetails"] = coursedetails

# Update JSON file with the additional details
writetojson(studentdetails)

# Read and print individual values from JSON file
readfromjson()
