#this is the starting variable for counting the loops that has been repeated
number = 0

#Start while loop statement
while True:
    number += 1

    # asks the user to press y to continue and q to quit
    choice = str(input("Press Y if you want to continue; Press Q to quit: "))

    #if the user press y the loop will continue
    if choice.upper() == 'Y':
        continue
    #if the user press q the loop will stop
    elif choice.upper() == 'Q':
        break
    #if the user press any key other than y and q it will print error and the number of loop will not change
    else:
        print("Error!")
        number = 0

print (f"\nThe loop repeated for {number} times.")