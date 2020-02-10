# insertion sort
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
import random

# Setting color parameters
rcParams['figure.facecolor'] = 'black'
rcParams['axes.facecolor'] = 'black'
rcParams['axes.labelcolor'] = 'white'

fig, ax = plt.subplots()

data = random.sample(range(100), 50)
x = list(range(len(data)))

comparisons = 0


def bubbleSort(fi):
    # Run throught all data elements
    for l in range(len(data)):
        for i, n in enumerate(data):
            if i < (len(data)) - 1:
                colors = list(len(data) * 'b')
                colors[i] = 'r'

                if n > data[i + 1]:
                    data[i] = data[i + 1]
                    data[i + 1] = n
                    plt.cla()

                    global comparisons
                    comparisons += 1

                    return plt.scatter(x, data, c=data, cmap='gist_rainbow'), plt.xlabel(
                        'Data size:50, {} comparisons'.format(comparisons))


ani = FuncAnimation(fig, bubbleSort, frames=500, interval=1)

ani.save('scatter_bubblesort3.gif', dpi=80, writer='imagemagick')

# plt.show()
print(data)
