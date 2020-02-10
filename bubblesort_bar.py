# bubble sort with bar graph
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
        # Compare all elements
        for i, n in enumerate(data):
            if i < (len(data)) - 1:
                # Change the color of the bars
                colors = list(len(data) * 'b')
                colors[i] = 'r'

                if n > data[i + 1]:
                    data[i] = data[i + 1]
                    data[i + 1] = n

                    plt.cla()

                    global comparisons
                    comparisons += 1
                    # Return plot
                    return plt.bar(x, data, color=colors), plt.xlabel(
                        'Data size{}, {} comparisons'.format(data_size, comparisons))


ani = FuncAnimation(fig, bubbleSort, frames=250, interval=1)

# To save the plot as gif install imagemagick
#ani.save('bar_bubblesort.gif', dpi=80, writer='imagemagick')

plt.show()
print(data)
