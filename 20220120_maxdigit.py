#Task: You have a number and you need to determine which digit in this number is the biggest.
def max_digit(integer):
    '''Takes an integer, returns the highest digit of that integer as type integer.'''
    return int(max(str(integer)))


if __name__ == '__main__':
    print("Example:")
    print(max_digit(940))

    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1