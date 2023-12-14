# range of number from 1 - 100
for multiples in range(1, 101):

    #numbers multiple of 3 and 5
    if multiples % 3 == 0 and multiples % 5 == 0:
        print('FizzBuzz\n')
    
    #numbers multiple of 3
    elif multiples % 3 == 0:
        print("Fizz\n")

    #numbers multiple of 5
    elif multiples % 5 == 0:
        print("Buzz\n")

    #numbers not multiple of 3 and 5
    else:
        print(multiples,"\n")