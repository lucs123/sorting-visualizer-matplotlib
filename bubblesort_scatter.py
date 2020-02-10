# bubble sort with scatter graph
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random

data_size = 30
data = random.sample(range(data_size), data_size)
x = list(range(len(data)))

fig = plt.figure()

comparisons = 0

def bubbleSort(fi):
    # Run throught all data elements
    for l in range(len(data)):
        # Compare elements
        for i, n in enumerate(data):
            if i < (len(data)) - 1:

                if n > data[i + 1]:
                    data[i] = data[i + 1]
                    data[i + 1] = n

                    plt.cla()

                    global comparisons
                    comparisons += 1

                    # Return plot
                    return plt.scatter(x, data, c=data, cmap='nipy_spectral'), plt.xlabel(
                        'Data size:{}, {} comparisons'.format(data_size,comparisons))


ani = FuncAnimation(fig, bubbleSort, frames=250, interval=1)

# To save the plot as gif install imagemagick
#ani.save('scatter_bubblesort.gif', dpi=80, writer='imagemagick')

plt.show()

print(data)
