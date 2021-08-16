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
https://user-images.githubusercontent.com/12467423/129532159-673c85c8-21c7-482a-ba00-f3e6cb3c6d5d.mp4
#### `/bin/bash`
https://user-images.githubusercontent.com/12467423/129532232-b6826dcd-103e-43b6-a923-ad201d61972a.mp4
#### Compressed Data
https://user-images.githubusercontent.com/12467423/129532398-77d5c70b-b5b8-4a58-a141-14e97d1e2a6e.mp4
#### JPEG Image
https://user-images.githubusercontent.com/12467423/129532381-eb024b02-6bc2-423d-bb1e-f06248cd6128.mp4
#### Raw Audio
https://user-images.githubusercontent.com/12467423/129532364-099aec4e-54ee-41b2-8483-83d9e2ce715d.mp4


