import numpy as np
from numba import njit

def get_ranks_numpy(arr):
    elems, counts = np.unique(arr, return_counts = True)
    unique_counts = np.unique(counts)
    get_rank = lambda elem: np.searchsorted(unique_counts, counts[np.searchsorted(elems, elem)])
    return np.vectorize(get_rank)(arr)

@njit
def get_ranks_numba(arr):
    arr = list(arr)
    print("Line 1")
    unique_elems = list(set(arr)) # unique_elems = np.unique(arr)
    print("Line 2")
#    counts = {elem: arr.count(elem) for elem in unique_elems}
    counts = {}
    for elem in unique_elems:
        counts[elem] = arr.count(elem)
    print("Line 3")
    sorted_counts = list(sorted(set(counts.values())))
    print("Line 4")
    return np.array([sorted_counts.index(counts[i]) for i in arr])

arr = np.array([2, 1, 2, 2, 9, 2, 3, 3, 4, 9, 2, 3, 8, 8, 3, 1, 7, 4, 7, 1, 8, 8, 6, 3, 6, 1, 4, 1, 1, 4, 3, 1, 7, 1, 4, 3, 2, 5, 4, 9, 1, 1, 3, 2])

arr2 = np.load("temp.npy")
