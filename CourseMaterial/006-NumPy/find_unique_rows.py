import numpy as np

a = np.array([
    [1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]])

# Ugly way:
a_contig = np.ascontiguousarray(a)
row_size = a.dtype.itemsize * a.shape[1]
whole_row_dtype = np.dtype((np.void, row_size))
a_array_of_rows = a_contig.view(whole_row_dtype)
_, idx = np.unique(a_array_of_rows, return_index=True)
unique_a = a[idx]

print unique_a

# Pretty way:
unique_row_tuples = {tuple(row) for row in a}
print np.vstack(unique_row_tuples)

# Vanilla - Python way
unique_row_tuples = {tuple(row) for row in a}
unique_row_lists = [list(row) for row in unique_row_tuples]
print np.array(unique_row_lists)
