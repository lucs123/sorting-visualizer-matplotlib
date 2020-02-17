from animate import Plot

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(data, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and data[i] < data[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and data[largest] < data[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap

        # Heapify the root.
        heapify(data, n, largest)
        Plot(i, data)
    # The main function to sort an array of given size


def heapSort(data):
    global i
    n = len(data)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(data, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # swap
        heapify(data, i, 0)




