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

#----------------------------------------------------------------------------------------------------------------------------------------
#                linear_1	linear_2    linear_3 sentinel	    binary_recursive binary	binary_iterative binary	    list.index()
#beginning	0 ms	        0 ms	    0 ms	            6302 ms	                280 ms	                    0.0
#middle	        1622 ms	        748 ms	    827 ms	            401 ms	                269 ms	                    0.0
#end 	        3176 ms	        1481 ms	    1802 ms	            12492 ms	                284 ms	                    0.0
#----------------------------------------------------------------------------------------------------------------------------------------

#Conclusions:

#By the looks of the results, a binary-iterative search is the most efficient, taking less time and less memory than all the other options.
#The reason recrusion is not too effective, in this case, is because it costs space, constantly recalling the function and redefining variables until we get the final result were looking for
#Of the three linear searches, the for-loop method is the most efficient because of how simple the code is and because it continues the loop until it reaches the final result
#Unlike this method, the the first and third methods consume slightly more memory because they both have variables to declare constantly, and compare with the value. We
#can conclude the the linear search methods can take a lot of time if the value is far into the list because it compares the elements one-by-one. The best case is if the
#value is at the begining of the list. Iterative Binary searches are more efficient because it continuesly splits the list in half until the item in the middle is equal to the searched value.
#It also has consistent delay no matter if the value is at teh begiining, middle or end.

