from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#xs = np.array([1,2,3,4,5,6], dtype = np.float64)
#ys = np.array([5,4,6,5,6,7] ,dtype = np.float64)


#creating sample random dataset
#withdatapoints,variance, step and correlation
def create_dataset(hm , variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y=val + random.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs= [i for i in range(len(ys))]
    return np.array(xs , dtype= np.float64), np.array(ys, dtype= np.float64)

xs, ys = create_dataset(40, 10, 2, correlation=False)

def best_fit_slope_and_intercept(xs, ys):
    m=( ((mean(xs)* mean(ys)) -mean(xs*ys))/
        ((mean(xs)**2)-mean(xs**2)) )
    c= mean(ys) - m * mean(xs)
    return m,c

def squared_errors(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)

def coeff_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr= squared_errors(ys_orig, ys_line)
    squared_error_y_mean= squared_errors(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)

m,c= best_fit_slope_and_intercept(xs, ys)

regression_line = [(m*x)+c for x in xs]

#to predict anything we can use the following
predict_x=8
predict_y=(m*predict_x) + c

#defining coeff. of determination
r_squared = coeff_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, s=100, color = 'r' )                                  #Red dot shows the item that is predicted.
plt.plot(xs, regression_line)
plt.show()
