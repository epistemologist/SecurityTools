import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
from tqdm import tqdm

def plot_bytes(filename):
    data = sys.stdin.buffer.read()
    bigrams = np.zeros((256,256), dtype=int)
    for i in tqdm(range(len(data)-1), colour="red"):
        bigrams[data[i]][data[i+1]] += 1
    print(np.max(bigrams), bigrams)
    plt.imshow(bigrams, cmap = "gnuplot2", vmin = 0, vmax = np.max(bigrams))
    plt.show()
    plt.savefig(filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Generates a bigram plot of bytes provided to stdin")
    parser.add_argument("-o", metavar = "filename", default = "plot.png", help = "Filename to write plot image")
    args = parser.parse_args()
    plot_bytes(args.o)
