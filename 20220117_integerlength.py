def integer_length(n):
    '''
    Takes an integer, returns the length of the given integer, e.g. the integer 24 has a length of 2
    '''
    integer_length = len(str(n))
    return integer_length


if __name__ == '__main__':
    assert integer_length(10) == 2
    assert integer_length(0) == 1

