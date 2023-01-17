#Lab-8_6

def factorial(num):
    """the factorial function"""
    count = 0
    product = 1
    #count and product to give the function values to start with
    while (count< num):
        count +=1
        product *= count
        #first the count increases, then the product of that is multiplied 
    return(product)

number= input("Enter a number: ")
print(factorial(number))
#Print statement for the function