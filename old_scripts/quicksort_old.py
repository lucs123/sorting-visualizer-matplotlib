import copy

def quicksort(data):
    # FRAME OPERATION BEGIN
    frames = [data]
    # FRAME OPERATION END
    ds = copy.deepcopy(data)
    qsort(ds, 0, len(data), frames)
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
