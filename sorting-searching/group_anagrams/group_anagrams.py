def group_anagrams(lst):
    """ Return list sorted by matching anagrams

    >>> group_anagrams(['balloon', 'call', 'phone', 'daft', 'fadt', 'tfda', 'llca', "llooban"])
    ['balloon', 'llooban', 'daft', 'fadt', 'tfda', 'call', 'llca', 'phone']

    """

    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)

    result = []
    for words in anagrams.values():
        result.extend(words)

    return result
