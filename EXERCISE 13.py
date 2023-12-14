def list(mylist):

    #set the value of product to 1
    product = 1

    #multiplies each value on the list below
    for i in mylist:
        product = product * i
    return product
    
#list of numbers to be multiplied    
numbers = [1,2,3,4,5]

#the product after multiplying the numbers
print(list(numbers))