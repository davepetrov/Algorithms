#David P
#Nov 14, 2018
#Sorting Algorithms (Simple)

def bubble_sort(lst):
    """(list) -> (list)
    Sorts a list in ascending order, in place (modifies it).

    >>> bubble_sort([2, 5, 1,-3])
    [-3, 1, 2, 5]
    >>> bubble_sort([3, 2, 2, 6, 5])
    [2, 2, 3, 5, 6]
    >>> bubble_sort([ ])
    []
    
    """
    for j in range(len(lst),1,-1):
        for i in range(1,j):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst

#----------------------------------------
def selection_sort(lst):
    """(list) -> (list)
    Sorts a list in ascending order, in place (modifies it).

    >>> selection_sort([2, 5, 1,-3])
    [-3, 1, 2, 5]
    >>> selection_sort([3, 2, 2, 6, 5])
    [2, 2, 3, 5, 6]
    >>> selection_sort([ ])
    []
    """
    for i in range(len(lst)):
        minimum = i
        for j in range(i+1,len(lst)):
            if lst[minimum]>lst[j]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
        
    return lst

#----------------------------------------
def insertion_sort(lst):
    """(list) -> (list)
    Sorts a list in ascending order, in place (modifies it).

    >>> insertion_sort([2, 5, 1,-3])
    [-3, 1, 2, 5]
    >>> insertion_sort([3, 2, 2, 6, 5])
    [2, 2, 3, 5, 6]
    >>> insertion_sort([ ])
    []
    """
    for i in range(0,len(lst)):
        index = lst.index(lst[i])
        while index > 0:
            if lst[index-1] > lst[index]:
                lst[index], lst[index-1] = lst[index-1], lst[index]
            index -= 1
            
    return lst
     
#----------------------------------------

def mergeSorted1(sortedA, sortedB):
    merged = []
    i = 0
    j = 0
    lenA = len(sortedA)
    lenB = len(sortedB)
    while i < lenA and j < lenB:
        if sortedA[i] <= sortedB[j]:
            merged.append(sortedA[i])
            i = i + 1
        else:
            merged.append(sortedB[j])
            j = j + 1
    merged.extend(sortedA[i:])
    merged.extend(sortedB[j:])
    return merged
    return right + left
            
def merge_sort(lst):
    """ (list) -> (list)
    Sorts a list in ascending order, in place (modifies it).

    >>> merge_sort([2, 5, 1,-3])
    [-3, 1, 2, 5]
    >>> merge_sort([3, 2, 2, 6, 5])
    [2, 2, 3, 5, 6]
    >>> merge_sort([3, 2, 2, 6, 5, -4, 12, 1, 2, 8 ,2, 7])
    [-4, 1, 2, 2, 2, 2, 3, 5, 6, 7, 8, 12]
    >>> merge_sort([ ])
    []
    """
    if len(lst) < 2:
        return lst
    
    middle = len(lst)//2
    start = 0
    end = len(lst)
    
    L = lst[start:middle]
    R = lst[middle:end]
    
    L = merge_sort(L)
    R = merge_sort(R)

    return mergeSorted1(L,R)

#----------------------------------------

def quick_sort(lst):
    """(list) -> (list)
    Sorts a list in ascending order, in place (modifies it).

    >>> quick_sort([2, 5, 1,-3])
    [-3, 1, 2, 5]
    >>> quick_sort([3, 2, 2, 6, 5])
    [2, 2, 3, 5, 6]
    >>> quick_sort([3, 2, 2, 6, 5, -4, 12, 1, 2, 8 ,2, 7])
    [-4, 1, 2, 2, 2, 2, 3, 5, 6, 7, 8, 12]
    >>> quick_sort([ ])
    []
    """
    if len(lst) < 2: return lst
    
    pivot = lst[0]
    smaller,greater,equal = [],[],[]
    
    for i in range(len(lst)):
        if pivot > lst[i]: smaller.append(lst[i])
        elif pivot < lst[i]: greater.append(lst[i])
        elif pivot == lst[i]: equal.append(lst[i])
            
    smaller, greater = quick_sort(smaller), quick_sort(greater)

    return (smaller+equal+greater)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

'''
---------------------------------------------------------------------------------------------------
    	        #    10	   |	      100	     |       1,000	     |	     10,000         
-----------------------------------------------------|---------------------------------------------
Bubble Sort	# 0   0	 0 | 0.002   0.002   0.004   | 0.17   0.32    0.43   | 18.00   33     47     
Selection sort	# 0   0	 0 | 0.001   0.001   0.002   | 0.11   0.15    0.12   | 10.30   10.8   11.4   
insertion sort	# 0   0	 0 | 0.002   0.003   0.004   | 0.198  0.30    0.411  | 20.1    30.2   44.7   
Merge sort	# 0   0	 0 | 0.001   0.002   0.001   | 0.013  0.017   0.014  | 0.144   0.188  0.142  
Quick sort	# 0   0	 0 | 0.004   0.001   0.004   | -----  0.015   -----  | -----   0.154  -----  
---------------------------------------------------------------------------------------------------

Of the simple sorting methods, we can conclude that Selection sort is the most consistent, no matter if the list is random, already
sorted or in reversed order. Bubble and insertion sorting methods are simply not sutitable for large data sets because it
continues to call the functions recursively until the list is sorted. Unlike selection sort, they consume lots of memory because of
the number of if statements the program must iterate through to reach its final objective; of being sorted. The reason to why Selection
sort is the most consistant of the simple sorting methods is because it constantly selects the minimum number in the list and
recursvely sets the list in order; again, without modifying the list after every comparison. Accoring to the collected data,
we can also conclude that all of the sorting methods are as effecient as one another when taking a small list as a
parameter; However,we can also conclude that the selection sort is most effecient and useful when trying to sort a large list.
Another reason to why it is the fastest is because it uses an exponential O(n) type.

Of the observed data, I am unable to indentify how efficient (or unefficient) the quick sorting is for the sorted trial and for the reverse
trial,for both, the list containing 1000 numbers and the list containing 10,000 numbers. This is because the program goes into a deep recursion.
We are, however, able to conclude that merge sort is extremely efficient because it uses the logerithmic O(n) type, making
it extremely quick and consistent when sorting.
'''

