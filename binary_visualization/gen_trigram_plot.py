import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse
import sys
from tqdm import tqdm

FIGURE_SIZE = (3.2,2.4)

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

def plot_bytes(filename):
    data = sys.stdin.buffer.read()
    trigrams = np.zeros((256,256,256), dtype=int)
    print("Generating trigrams...")
    for i in tqdm(range(len(data)-3), colour='red'):
        trigrams[data[i], data[i+1], data[i+2]] += 1
    trigrams = trigrams.reshape((256**3))
    non_empty_trigrams = np.nonzero(trigrams)[0]
    print(non_empty_trigrams.shape)
    fig = plt.figure(figsize=FIGURE_SIZE, facecolor="black")
    ax = fig.add_subplot(111, projection='3d')
    ax.axis("off")
    X, Y, Z = gen_xyz_arrs()
    print(X[non_empty_trigrams])
    def init_plot():
        print("Plotting points...")
        ax.scatter(X[non_empty_trigrams], Y[non_empty_trigrams], Z[non_empty_trigrams], c=trigrams[non_empty_trigrams], cmap = "gnuplot2", alpha = 0.5, s = 2, vmin = 0, vmax = np.max(trigrams))
        print("Done plotting points!")
        return fig,
    def animate_plot(i):
        ax.view_init(45,i)
        return fig,
    print("Animating plot and saving video...")
    anim = animation.FuncAnimation(fig, animate_plot, frames = tqdm(range(360), colour="red"), init_func = init_plot, interval=20, blit=True)
    anim.save(filename, fps=30)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Generates a bigram plot of bytes provided to stdin")
    parser.add_argument("-o", metavar = "filename", default = "animation.mp4", help = "Filename to write video of plot to")
    args = parser.parse_args()
    plot_bytes(args.o)
