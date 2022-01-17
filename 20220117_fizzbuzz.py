def fizzbuzz(n):
    '''
    Takes integer n, returns string depending on integer value 
    '''
    if (n % 3 == 0) and (n % 5 ==0):
        return 'FizzBuzz'
    if n % 3 == 0: 
        return 'Fizz'
    elif n % 5 == 0: 
        return 'Buzz'
    
    
    
if __name__ == '__main__':
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
