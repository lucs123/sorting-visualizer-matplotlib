from quicksort import partition
from animate import Plot


def heapify(unsorted, index, start, end):
    heap_size = end + 1 - start
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[start + left_index] > unsorted[start + largest]:
        largest = left_index

    if right_index < heap_size and unsorted[start + right_index] > unsorted[start + largest]:
        largest = right_index

    if largest != index:
        unsorted[start + largest], unsorted[start + index] = unsorted[start + index], unsorted[start + largest]
        heapify(unsorted, largest, start, end)
        Plot(largest,unsorted)


def heapSort(unsorted, start, end):
    n = end + 1 - start
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, start, end)
    for i in range(end, start, -1):
        unsorted[start], unsorted[i] = unsorted[i], unsorted[start]
        heapify(unsorted, 0, start, i - 1)
    return unsorted


def introSort(data, start, end, depth):
    if start < end:
        if depth == 0:
            # Switch from quicksort to heapsort
            heapSort(data, start, end)
            Plot(max(data[start:end + 1]), data)
            return
        
        # Return the pivot index
        p = partition(data, start, end)

        # Sort all the elements to the left and to the right of the pivot
        introSort(data, start, p - 1, depth - 1)
        introSort(data, p + 1, end, depth - 1)

