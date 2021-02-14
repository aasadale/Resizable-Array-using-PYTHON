# Resizable-Array / Dynamic Array, Python

#### Resizable arrays are mutable arrays which can grow and shrink according to our need. In resizable array, we don't need to declear size of array, as we did in static arrays.

#### This file consists of the following Functions/Methods:

1) **Insert_Value()** Insert value simply appends the value/item to index 0 and so on. Initial lenght of array is 2, and when we push two elements at index 0 and 1, it will                             increase its size by multiplying its intital lenght with growth factor. So here the growth factor is 2. So if we append the third element, a new array of                           lenght 4 will be created in which above elements will be copy to its similar indexes, now we have two more spaces to push elements and that how Insert value                       function works.

2) **Insert_At_First()** This function simply insert the value at first index , i.e 0 index

3) **Insert_At_End()**   Insert_At_End will inserts the value at last index.

4) **Delete_At_First()** \n This function will delete the first value of an array.

5) **Delete_At_Last()**  This function will delete the last value of an array.

6) **Shrink_Array()**    This function will delete the last value of an array. Suppose we have an array of lenght 16, in which we have elements till 8th index. Rest of the array                            is containing empty memory blocks. Suppose we again call the shrink function, it will delete the element at index 8 and here an empty memory block will                            be created. Now as element of 8th index is also deleted so half of the array is now empty containing empty memory blocks, So at this stage, array will                              shrink its size to half, and only return elements from 0 to 7th index which is of lenght 8. So this function will delete the last element of array and                              will shrink its size to half when half array is empty and half contains elements.
