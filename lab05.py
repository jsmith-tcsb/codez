## Mutable Lists ##

# Q1
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    #"*** YOUR CODE HERE ***"
    i = 0
    while i<len(lst):
        lst[i] = fn(lst[i])
        i=i+1
    return (lst)


a = [1, 2, 3, 4, 5]
def over_nine_thousand(original_list):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> over_nine_thousand(original_list)
    >>> original_list
    [9001, 9002, 9003, 9004, 9005]
    """
    #"*** YOUR CODE HERE ***"
    i = 0
    while i<len(lst):
        lst[i] = lst[i]+9000
        i=i+1
    return (lst)

over_nine_thousand(a)

## Dictionaries ##

# Q4
def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"

## Nonlocal ##

# Q5
def count_calls(f):
    """A function that returns a version of f that counts calls to f and can
    report that count to how_many_calls.


    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    "*** YOUR CODE HERE ***"
