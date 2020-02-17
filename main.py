import random
from quicksort import quickSort
from bubblesort import bubbleSort
from animate import camera, alg_name, graph_name, graphs
import matplotlib.pyplot as plt

try:
    data_size = int(input('Data size(defaut 30):'))
except ValueError:
    data_size = 30

data = random.sample(range(data_size), data_size)

algorithms = {'1': bubbleSort,
              '2': quickSort}

i = input('Select the algorithm(1 for bubbleSort, 2 for quickSort):')
if i not in algorithms:
    i = '2'

g = input('Select the graphic(1 for bar, 2 for scatter):')
if g not in graphs:
    g = '1'

save = input('Do you want to save the graph(y|n):')
if save == 'y':
    save = True

graph_name(g)
alg_name(i)

func = algorithms[i]

if func == quickSort:
    func(data, 0, len(data) - 1)
elif func == bubbleSort:
    func(data)

animation = camera.animate()

if save:
    #animation.save('animation.gif', dpi=60, writer='imagemagick')
    animation.save('animation.mp4')

plt.show()
