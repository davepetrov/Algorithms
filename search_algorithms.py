#David P
#Nov 14, 2018
#Search algorithms w/ for loops, while loops, sentinel search, recrursion and iterative
#---------------------------------------------------------Linear Search Algorithms---------------------------------------------------------#

#1 - W/ while loop
def linear_search1(lst,value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search1([2, 5, 1, -3], 2)
    0
    >>> linear_search1([0, 5, 2, 1, -3], 2)
    2
    >>> linear_search1([2, 5, 1, -3], -3)
    3
    >>> linear_search1([2, 5, 1, -3], -5)
    -1
    >>> linear_search1([2, 5, 1, -3], 9)
    -1
    >>> linear_search1([2, 5, 1, -3], 4)
    -1
    >>> linear_search1([], 4)
    -1
    >>> linear_search1([1], 4)
    -1
    >>> linear_search1([4, 2, 5, 1, -3, 4], 4)
    0
    
    """
    index=0
    while index < len(lst) and lst[index] != value:
        index+=1
    if index == len(lst):
        return -1
    return index

def linear_search2(lst,value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search2([2, 5, 1, -3], 2)
    0
    >>> linear_search2([0, 5, 2, 1, -3], 2)
    2
    >>> linear_search2([2, 5, 1, -3], -3)
    3
    >>> linear_search2([2, 5, 1, -3], -5)
    -1
    >>> linear_search2([2, 5, 1, -3], 9)
    -1
    >>> linear_search2([2, 5, 1, -3], 4)
    -1
    >>> linear_search2([], 4)
    -1
    >>> linear_search2([1], 4)
    -1
    >>> linear_search2([4, 2, 5, 1, -3, 4], 4)
    0
    """
    for index in range(len(lst)):
        if lst[index]==value:
            return index
    return -1



def linear_search3(lst,value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search3([2, 5, 1, -3], 2)
    0
    >>> linear_search3([0, 5, 2, 1, -3], 2)
    2
    >>> linear_search3([2, 5, 1, -3], -3)
    3
    >>> linear_search3([2, 5, 1, -3], -5)
    -1
    >>> linear_search3([2, 5, 1, -3], 9)
    -1
    >>> linear_search3([2, 5, 1, -3], 4)
    -1
    >>> linear_search3([], 4)
    -1
    >>> linear_search3([1], 4)
    -1
    >>> linear_search3([4, 2, 5, 1, -3, 4], 4)
    0
    """
    lst.append(value)
    index=0
    while lst[index] != value:
        index+=1
    lst.pop()
    if index == len(lst):
        return -1
    return index

#---------------------------------------------------------Binary Search Algorithms---------------------------------------------------------#

def binary_search_recursive(lst, value, left, right):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> binary_search_recursive([-3, 1, 2, 5], 5, 0, 3)
    3
    >>> binary_search_recursive([2, 2, 4, 5], 2,0,3)
    1
    >>> binary_search_recursive([-3, 1, 2, 5], 4, 0, 3)
    -1
    >>> binary_search_recursive([], 5, 0, 0)
    -1
    """
    lst.sort()
        
    if left > right or value not in lst:
        return -1
    middle = (left+right)//2
    if lst[middle] == value:
        return middle
    if value > lst[middle]:
        return binary_search_recursive(lst, value, middle+1, right)
    return binary_search_recursive(lst, value, left, middle-1)
    
def binary_search_iterative(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> binary_search_iterative([-3, 1, 2, 5], 5)
    3
    >>> binary_search_iterative([2, 2, 4], 2)
    1
    >>> binary_search_iterative([-3, 1, 2, 5], 4)
    -1
    >>> binary_search_iterative([], 5)
    -1
    """
    lst.sort()

    left, right = 0, len(lst)-1
    while not left > right:
        middle = (left+right)//2
        if value == lst[middle]:
            return middle
        elif value < lst[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

