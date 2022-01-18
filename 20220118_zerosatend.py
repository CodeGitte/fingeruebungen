def end_zeros(int):
    '''Takes a positive integer, returns the count of zeros at the end of the integer'''
    return len(str(int)) - len(str(int).rstrip('0'))


if __name__ == '__main__':
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2