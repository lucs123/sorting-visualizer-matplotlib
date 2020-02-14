import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import copy
import main

data = random.sample(range(10), 10)
x = list(range(len(data)))


def quick_sort(data_set):
	# FRAME OPERATION BEGIN
	frames = [data_set]
	# FRAME OPERATION END
	ds = copy.deepcopy(data_set)
	qsort(ds, 0, len(data_set), frames)
	# FRAME OPERATION BEGIN
	frames.append(ds)
	return frames
	# FRAME OPERATION END


def qsort(ds, head, tail, frames):
	if tail - head > 1:
		# FRAME OPERATION BEGIN
		ds_y = copy.deepcopy(ds)

		# FRAME OPERATION END
		i = head
		j = tail - 1
		pivot = ds[j]
		while i < j:
			# FRAME OPERATION BEGIN
			frames.append(copy.deepcopy(ds_y))

			# FRAME OPERATION END
			if ds[i] > pivot or ds[j] < pivot:
				ds[i], ds[j] = ds[j], ds[i]
				# FRAME OPERATION BEGIN
				ds_y[i], ds_y[j] = ds_y[j], ds_y[i]
				frames.append(copy.deepcopy(ds_y))

				# FRAME OPERATION END
			if ds[i] == pivot:
				j -= 1
			else:
				i += 1
		qsort(ds, head, i, frames)
		qsort(ds, i + 1, tail, frames)


fig = plt.figure()

index = 0

def animate(i):
	global index

	frames = quick_sort(data)
	bars = frames[index]
	index +=1

	plt.cla()
	return plt.bar(x, bars)


# ani = animate(50)
ani = FuncAnimation(fig, animate, frames=50, interval=1)
plt.show()
