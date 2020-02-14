import copy
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = random.sample(range(10), 10)
x = list(range(len(data)))

fig = plt.figure()

colors = list(len(data) * 'b')

def bubble_sort(data):
    # FRAME OPERATION BEGIN
    frames = [data]
    # FRAME OPERATION END
    ds = copy.deepcopy(data)
    for i in range(10 - 1):
        flag = False
        for j in range(10 - i - 1):
            if ds[j] > ds[j + 1]:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]
                flag = True
            # FRAME OPERATION BEGIN
            frames.append(copy.deepcopy(ds))

            # FRAME OPERATION END
        if not flag:
            break
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames


index = 0


def animate(i):
    global index

    frames = bubble_sort(data)
    bars = frames[index]
    index += 1

    plt.cla()
    return plt.bar(x, bars)


# ani = animate(50)
ani = FuncAnimation(fig, animate, frames=50, interval=1)
plt.show()
