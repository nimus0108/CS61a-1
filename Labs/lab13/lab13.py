""" Lab 13: Final Review """

# Q3
def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return
    else:
        if len(lst) == 1:
            yield lst
        else:
            for i in range(len(lst)):
                num = lst[i]
                before_and_after = lst[:i] + lst[i+1:]
                before_and_after = list(before_and_after)
                print(before_and_after)
                for p in permutations(before_and_after):
                    yield [num] + p
