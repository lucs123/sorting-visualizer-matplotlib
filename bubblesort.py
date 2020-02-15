# bubble sort with bar graph
from animate import Plot

def bubbleSort(data):
    # Run throught all data elements
    for l in range(len(data)):
        # Compare all elements
        for i, n in enumerate(data):
            if i < (len(data)) - 1:
                # Change the color of the bars

                if n > data[i + 1]:
                    data[i] = data[i + 1]
                    data[i + 1] = n

                    Plot(i + 1, data)

