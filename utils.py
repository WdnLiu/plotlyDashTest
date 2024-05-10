import base64
import io
import matplotlib.colors as mcolors
from matplotlib import patches, pyplot as plt
import numpy as np

def save_boolean_matrix(bool_matrix, save_path):
    n, m = bool_matrix.shape
    matrix_with_spacing = np.zeros((n*2-1, m), dtype=bool)
    matrix_with_spacing[::2] = bool_matrix
    matrix_with_spacing[1::4] = False  # Set every second row to False (white)
    cmap = mcolors.ListedColormap(['white', 'darkgrey'])
    plt.imshow(matrix_with_spacing, cmap=cmap, interpolation='nearest')
    plt.xlabel('Timestamps')
    plt.ylabel('Instruments')
    plt.yticks(np.arange(0, 2 * n, 2), np.arange(1, n + 1))
    plt.title('Result of instrument classification')
    plt.savefig(save_path)