def compress_str(string):
    """ Create a compressed version of a string

        >>> compress_str("aaabbccc")
        'a3b2c3'

        >>> compress_str("abcde")
        'abcde'

    """

    new_str = string[0]
    count = 1

    for i in range(len(string) - 1):
        if string[i + 1] == string[i]:
            count += 1
        else:
            new_str += str(count) + string[i + 1]
            count = 1

    new_str += str(count)

    if len(string) < len(new_str):
        return string
    else:
        return new_str
