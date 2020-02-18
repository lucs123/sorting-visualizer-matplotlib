# Matplotlib sorting visualizer
Scripts to visualize sorting algorithms using matplotlib animations
### Bar graph
![](gifs/bubblesort_bar2.gif)
![](gifs/quicksort_bar.gif)

### Scatter graph
![](gifs/bubblesort_scatter2.gif)
![](gifs/quicksort_scatter.gif)

## Algorithms available
|Algorithm    | Best case | Worst case | Average case
|-------------|-----------|------------|---------------
|Bubble sort  | O(n)      |     O(n2)  |O(n^2)       |
|Quick sort   |           |            |
|Heap sort    |           |            |

## About
This project aims to make sorting algorithms easier to visualize and understand, it is a series of standalone scripts so there's
some repeated code in them.  
It's still at early development so there is only bubblesort algoritm at the moment, more algorithms will be added.
### Dependencies
- Matplotlib
- Image magick(Only needed to save as gif, graph can also be saved as mp4)
