def easy_unpack(tuple): 
    """Takes a tuple, returns a tuple with 3 elements (first, third and second to the last)."""
    return tuple[0], tuple[2], tuple[-2]

if __name__ == '__main__':
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)