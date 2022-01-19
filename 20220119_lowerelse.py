def lower_else(str):
    '''Takes a string, returns 'False' if string contains any lowercase, else returns 'True'.''' 
    if not str:
        return True #returns True if str is empty
    elif any(i.islower() for i in str):
        return False #returns False if str contains any lowercase
    else: 
        return True #returns True for everything else
        
        
    
        
if __name__ == '__main__':
    print("Example:")
    print(lower_else('ALL UPPER'))

    assert lower_else('ALL UPPER') == True
    assert lower_else('all lower') == False
    assert lower_else('Beginning with') == False
    assert lower_else('mixed UPPER and lower') == False
    assert lower_else('') == True
    assert lower_else('444') == True
    assert lower_else('55 55 5') == True