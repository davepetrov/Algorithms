## Results
| linear_1 | linear_2 | linear_3 sentinel | binary_recursive binary | binary_iterative binary | list.index() |
| --- | | --- | | --- | | --- | | --- | | --- | 
| beginning | 0 ms | 0 ms |  0 ms | 6302 ms | 280 ms | 0.0 |
| middle | 1622 ms | 748 ms | 827 ms | 401 ms | 269 ms | 0.0 |
| end | 3176 ms | 1481 ms | 1802 ms | 12492 ms | 284 ms | 0.0 |


n                           #      10      |               100                 |            1,000            |         10,000         
Bubble Sort          # 0   0     0 | 0.002   0.002   0.004   | 0.17   0.32    0.43      | 18.00   33     47     
Selection sort       # 0   0     0 | 0.001   0.001   0.002   | 0.11   0.15    0.12      | 10.30   10.8   11.4   
insertion sort        # 0   0     0 | 0.002   0.003   0.004   | 0.198  0.30    0.411   | 20.1    30.2   44.7   
Merge sort           # 0    0     0 | 0.001   0.002   0.001   | 0.013  0.017   0.014  | 0.144   0.188  0.142  
Quick sort            # 0    0     0 | 0.004   0.001   0.004   | -----    0.015   -----    | -----   0.154  -----  

## Conclusions:

Binary-iterative search is the most efficient, taking less time and less memory than all the other options. The reason recrusion is not too effective, in this case, is because it costs quite the space, constantly recalling the function and redefining variables for every stack call until we get the final result were looking for. By the results, we conclude that the linear search methods can take a lot of time if the value is far into the list because it compares the elements one-by-one,  linearly from the first index. The best case is if the value is at the begining of the list with a complexity of O(1), trivially. Iterative Binary searches  are more efficient because they continuesly splits the list in half until the item in the middle is equal to the searched value.

Accoring to the collected data, we can  conclude that all of the simple sorting methods are as effecient as one another when taking given a small data set  All of the simple sorting algorithms require a time complexity of O(n^2), which is not suitable for large sets. The time complexity increases very quickly with large data sets. Of the observed data, I am unable to indentify how efficient (or unefficient) the quick sorting is for the sorted trial and for the reverse trial, for both, the list containing 1000 numbers and the list containing 10,000 numbers (ie: With large data sets). This is because the program goes into a deep recursion. We are, however, able to conclude that merge sort is extremely efficient because it requires a stable average and worst case time compelxity of O(nlogn), an ideal complexity for sorting. Quick sort requires a time complexity an average time complexity of O(nlogn) and the worst complexity of O(n^2), similair to the simple sorting algorthms discussed previously. This is because on average, the algorithm would choose a pivot near the middle of the data set, similair merge-sort's choice of pivots. Worst case cenario, we would be picking the smallest or largest value in the dataset every time which would translate to a time compelity of O(n^2)
