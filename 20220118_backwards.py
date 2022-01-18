def backwards(str):
    'Takes a string, returns it backwards.'
    return str[::-1]


if __name__ == '__main__':
    assert backwards('Hello World') == 'dlroW olleH'
    assert backwards('Aloha') == 'aholA'