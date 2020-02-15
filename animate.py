import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
comparisons = 0

titles = {'1': "Bubblesort algorithm",
          '2': 'Quicksort algorithm'}
title = ''

graphs = {'1': plt.bar,
          '2': plt.scatter}

def alg_name(alg):
    global title
    title = titles[alg]
    return title

def graph(gph):
    global graph
    graph = graphs[gph]
    return graph

def Plot(highlight, data):
    colors = list(len(data) * 'b')
    colors[highlight] = 'g'
    x = list(range(len(data)))
    global comparisons
    comparisons += 1
    plt.title(title)
    plt.xlabel('Data size:{}, Number of comparisons:{}'.format(len(data), comparisons))
    graph(x, data, color=colors)
    camera.snap()
