from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype = np.float64)
ys = np.array([5,4,6,5,6,7] ,dtype = np.float64)

def best_fit_slope_and_intercept(xs, ys):
    m=( ((mean(xs)* mean(ys)) -mean(xs*ys))/
        ((mean(xs)**2)-mean(xs**2)) )
    c= mean(ys) - m * mean(xs)
    return m,c

m,c= best_fit_slope_and_intercept(xs, ys)
print(m,c)

regression_line = [(m*x)+c for x in xs]

#to predict anything we can use the following
predict_x=8
predict_y=(m*predict_x) + c

print(predict_y)
plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, color = 'r' )                                  #Red dot shows the item that is predicted.
plt.plot(xs, regression_line)
plt.show()
