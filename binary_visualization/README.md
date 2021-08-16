# Binary Visualization Tools

Various scripts that can be used to visualize raw binary data

## Inspirations
 - [This blog post](https://codisec.com/binary-visualization-explained/) was the main inspiration for the 2D and the 3D plotting scripts - in fact, many of the ideas in this and other blog posts from the developers of Veles were used here.


## Digrams
The script `gen_bigram_plot.py` generates a plot of the most common byte bigrams in the given data provided to stdin.

### Example Plots

#### ASCII Text
![2D ASCII plot](/binary_visualization/plots/2d_ascii.png)
#### Compressed Data
![2D Compressed plot](/binary_visualization/plots/2d_compressed.png)

## Trigrams
The script `gen_trigram_plot.py` generates a plot of the most common byte trigrams in the given data provided to stdin. Note that due to the added dimension, this takes *a lot* longer than the 2D plots, but gives a lot more resolution.

#### ASCII Text
![3D ASCII plot](/binary_visualization/plots/3d_ascii.mp4)
