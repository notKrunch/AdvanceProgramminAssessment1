# Function to open the text file and stores the data into a list
def readnumbers():
    with open('C:/Users/mrlum/Desktop/L5 ADVANCED PROGRAMMING 1ST SEM/ASSESSMENT 1/CHAPTER 4/numbers.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

numbers = readnumbers()
print(numbers)