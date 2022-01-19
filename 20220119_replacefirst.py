#Task: In a given list the first element should become the last one. 
#An empty list or list with only one element should stay the same.

def replace_first(list):
    '''Takes a list, returns same list if len(list) == 0 or 1; else returns modified list where first element becomse the last one'''
    if not list: #list is empty
        return list
    elif len(list) == 1: #length of list is equal to 1, return list
        return list
    elif len(list) > 1: #length of list is more than 1, given list the first element should become the last one. 
        first = list[0]
        modified_list = list[1:]
        modified_list.append(first)
        return modified_list


if __name__ == "__main__":
    print("Example:")
    print(replace_first([1, 2, 3, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []