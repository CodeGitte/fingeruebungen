def remove_all_before(list, int):
    '''Takes a list and an integer, returns a shortened list where all elements before the integer are removed if the integer is part of the list.
    If the integer is not in the list, the list remains the same'''
    for i in list:
        if (i == int):
            return list[list.index(i):]
    else:
        return list



if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]