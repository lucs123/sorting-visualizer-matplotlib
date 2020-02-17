from animate import Plot

def bubbleSort(data):
    # Run throught all data elements
    for l in range(len(data)):
        # Compare all elements
        for i in range(len(data)):
            if i < (len(data)) - 1:
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]

                    Plot(i + 1, data)

