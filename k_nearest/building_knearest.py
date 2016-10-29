import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

#using numpy as it is faster
#euclidean_distance = sqrt ((plot1[0]-plot2[0])**2+(plot1[1]-plot2[1])**2)
#dictionary dataset

dataset = {'k': [[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]
