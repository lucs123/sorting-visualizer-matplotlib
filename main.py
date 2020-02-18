import random
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort
from animate import camera, alg_title, graph_title, graphs
import matplotlib.pyplot as plt

try:
    data_size = int(input('Data size(defaut 30):'))
except ValueError:
    data_size = 30

data = random.sample(range(data_size), data_size)

algorithms = {'1': bubbleSort,
              '2': quickSort,
              '3': heapSort}

alg = input('Select the algorithm(1 for bubbleSort, 2 for quickSort, 3 for heapSort):')
if alg not in algorithms:
    alg = '2'

gph = input('Select the graph(1 for bar, 2 for scatter):')
if gph not in graphs:
    gph = '1'

save = input('Do you wanna save(y|n):')
if save == 'y':
    save = True

graph_title(gph)
alg_title(alg)

func = algorithms[alg]

if func == quickSort:
    func(data, 0, len(data) - 1)
elif func == bubbleSort or heapSort:
    func(data)

interval_time = 20
animation = camera.animate(interval=interval_time)

# To save as gif install imagemagick, to save as mp4 install ffmpeg(if not already installed)
if save:
    #animation.save('animation.gif', dpi=60, writer='imagemagick')
    animation.save('animation.mp4')

plt.show()
