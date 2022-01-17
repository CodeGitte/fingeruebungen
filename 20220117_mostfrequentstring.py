def most_frequent(list):
    """
    takes a list of strings 
    returns the most frequent string within the list 
    """
    most_frequent = max(list, key = lambda x: list.count(x))
    return most_frequent


if __name__ == "__main__":      
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

