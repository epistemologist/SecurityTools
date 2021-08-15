import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from matplotlib import animation
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numba import njit
import argparse
import sys
from tqdm import tqdm
from collections import Counter

FIGURE_SIZE = (3.2*6,2.4*6)

def gen_xyz_arrs():
    try:
        arrs = np.load("~/arrs.npz")
        X = arrs['X']; Y = arrs['Y']; Z = arrs['Z']
        return X,Y,Z
    except:
        X = np.stack([np.ones((256,256), dtype=int)*i for i in range(256) ]).reshape((256**3))
        Y = np.stack([np.column_stack([range(256) for j in range(256)]) for i in range(256)]).reshape(256**3)
        Z = np.stack([np.vstack([range(256) for j in range(256)]) for i in range(256)]).reshape((256**3))
        np.savez(open("arrs.npz", "wb"), X=X, Y=Y, Z=Z)
        return X, Y, Z

@njit
def get_ranks(arr):
    arr = list(arr)
    unique_elems = list(set(arr))
    counts = {}
    for elem in unique_elems:
        counts[elem] = arr.count(elem)
    sorted_counts = list(sorted(set(counts.values())))
    return np.array([sorted_counts.index(counts[i]) for i in arr])

def plot_bytes(filename, num_points):
    # Read in bytes and generate trigrams
    data = sys.stdin.buffer.read()
    trigrams = np.zeros((256,256,256), dtype=int)
    print("Generating trigrams...")
    for i in tqdm(range(len(data)-3), colour='red'):
        trigrams[data[i], data[i+1], data[i+2]] += 1
    trigrams = trigrams.reshape((256**3))
    # Rank trigrams (for coloring the plot)
    print("Ranking trigrams...")
    trigrams_ranks = get_ranks(trigrams)
    elems, counts = np.unique(trigrams, return_counts = True)
    # Get max n trigrams (as given by parameter)
    max_count = np.sort(trigrams)[-num_points]
    top_trigram_indices = np.where(trigrams >= max_count)[0]
    print(top_trigram_indices.shape)
    # Set up plot
    rcParams["figure.facecolor"] = "black"
    rcParams["savefig.facecolor"] = "black"
    rcParams["axes.facecolor"] = "black"
    fig = plt.figure(figsize=FIGURE_SIZE, facecolor="black")
    ax = fig.add_subplot(111, projection='3d')
    ax.axes.set_xlim3d(left=-0.5, right=256.5)
    ax.axes.set_ylim3d(bottom=-0.5, top=256.5)
    ax.axes.set_zlim3d(bottom=-0.5, top=256.5)
    ax.axis("off")
    # Generate color scheme for plot
    cm_arr = cm.gnuplot2_r(np.linspace(0, 1, 256))
    cm_arr[:, 3] = np.linspace(1, 0, 256)
    new_cm = ListedColormap(cm_arr)
    # Plot the image
    X, Y, Z = gen_xyz_arrs()
    def init_plot():
        print("Plotting points...")
        ax.scatter(X[top_trigram_indices], Y[top_trigram_indices], Z[top_trigram_indices], c=get_ranks(trigrams[top_trigram_indices]), cmap = new_cm, alpha = 0.8, s = 1)
        print("Done plotting points!")
        return fig,
    def animate_plot(i):
        ax.view_init(45,i)
        return fig,
    print("Animating plot and saving video...")
    anim = animation.FuncAnimation(fig, animate_plot, frames = tqdm(range(0, 90, 2), colour="red"), init_func = init_plot, interval=20, blit=True)
    anim.save(filename, fps=15)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Generates a trigram plot of bytes provided to stdin")
    parser.add_argument("-o", metavar = "filename", default = "animation.mp4", help = "Filename to write video of plot to")
    parser.add_argument("-n", type = int, metavar = "num_points", default = 100000, help = "Only plot top n points (to avoid plotting a giant block)")
    args = parser.parse_args()
    plot_bytes(args.o, args.n)
