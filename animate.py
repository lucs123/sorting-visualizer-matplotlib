import matplotlib.pyplot as plt
from celluloid import Camera


fig = plt.figure()
camera = Camera(fig)
comparisons = 0

def graph(highlight,data):
    colors = list(len(data) * 'b')
    colors[highlight] = 'g'
    x = list(range(len(data)))
    global comparisons
    comparisons+=1
    plt.title('Bubblesort algorithm')
    plt.xlabel('Data size:{}, Number of comparisons:{}'.format(len(data), comparisons))
    plt.bar(x, data, color=colors)
    camera.snap()




