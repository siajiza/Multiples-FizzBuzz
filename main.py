

def multiples(numbers):
 
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            numbers += 1
            print('fizzbuzz')
            continue   
        elif numbers % 3 == 0:
            numbers += 1
            print('fizz')
            continue    
        elif numbers % 5 == 0:   
            numbers += 1
            print('buzz')
            continue    
        else:
            print(numbers)            
    return numbers


multiples(101)
