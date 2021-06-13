# Matplotlib sorting visualizer
Scripts to visualize sorting algorithms using matplotlib animations
### Bar graph
![](gifs/bubblesort_bar2.gif)
![](gifs/quicksort_bar.gif)

### Scatter graph
![](gifs/bubblesort_scatter2.gif)
![](gifs/quicksort_scatter.gif)

## Algorithms available
- Bubble sort
- Quick sort
- Heap sort
- Intro sort

## About
The aim of this project is to make sorting algorithms easier to visualize and understand, using the animation capabilities of matplotlib.  

### Dependencies
- Python 3.6+
- Matplotlib
- Celluloid module(https://github.com/jwkvam/celluloid)
- Image magick to save as gif or ffmpeg to save as mp4

### Manual
- Install Matplotlib and Celluloid(if not already installed)
`pip install celluloid`
`pip install matplotlib`

- Install ImageMagick or ffmpeg(optional)

- Run main.py

`python main.py`

0. (To run with defaut values just press enter)
1. Select Data size(default 30)
2. Select the algorithm(defaut is quicksort)
3. Select the type of graph(defaut bar graph)
4. Choose if you want to save

### How to contribute
1. Put new algorithm on root
1. Import Plot from animate
1. Use Plot function in algorithm function
1. Add algorithm to algorithms in main file
1. Add algorithm title in animate file
