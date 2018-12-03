def has_additive_sequence(string: str) -> bool:
    """Checks whether a given string has additive sequence returns true if it contains
    additive sequence and false otherwise
    @type string: str
    @rtype:bool
    >>> has_additive_sequence("1,2,3,5")
    >>> True
    >>> has_additive_sequence("1,2,3,4")
    >>> False
    >>> has_additive_sequence("1235")
    >>> True
    >>> has_additive_sequence("12345")
    >>> False
    """
    digit_list = []
    if string.isdigit():
        for digit in string:
            digit_list.append(digit)
    else:
        digit_list = string.split(',')
    count = 0
    while count < len(digit_list) - 3:
        if sum([int(digit) for digit in digit_list[count:count+2]]) != int(digit_list[count + 2]):
            return False
        count += 1
    return True
