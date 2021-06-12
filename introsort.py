from quicksort import partition
from heapsort import heapSort
from animate import Plot

def introSort(data, start, end, depth):
    if start < end:
        if depth == 0:
            # Switch from quicksort to heapsort
            tmp = data[start:end + 1]
            heapSort(tmp)
            data[start:end + 1] = tmp
            Plot(max(tmp), data)
            return
        
        # Return the pivot index
        p = partition(data, start, end)

        # Sort all the elements to the left and to the right of the pivot
        introSort(data, start, p - 1, depth - 1)
        introSort(data, p + 1, end, depth - 1)