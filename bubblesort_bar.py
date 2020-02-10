# bubble sort
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random

data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#data = random.sample(range(70), 30)
x = list(range(len(data)))

fig = plt.figure()

comparisons = 0

def bubbleSort(fi):

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

                    return plt.bar(x, data, color=colors), plt.xlabel('{} comparisons'.format(comparisons))


ani = FuncAnimation(fig, bubbleSort, frames=100, interval=1)

ani.save('bar_bubblesort2.gif', dpi=80, writer='imagemagick')
#plt.show()
print(data)
