import random
from quicksort import quickSort
from bubblesort import bubbleSort
from animate import camera
import matplotlib.pyplot as plt

data_size = 30
data = random.sample(range(data_size), data_size)
x = list(range(len(data)))

#quickSort(data, 0, len(data) - 1)
bubbleSort(data)

animation = camera.animate()
#animation.save('animation.gif', dpi=80, writer='imagemagick')
plt.show()