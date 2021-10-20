import matplotlib.pyplot as plt
import numpy as np
import math


def plot(x: list[float], x_points: list[float], save: bool = False):
    # the function, which is y = 2^2+10-10cos(2πx)
    y = x**2+10-10*np.cos(2*math.pi*x)

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x, y, 'y', label='y=2^2+10-10cos(2πx)')

    ax.plot(x_points[0], x_points[0]**2+10-10*np.cos(2*math.pi*x_points[0]), 'o-', color='red')
    for x in x_points[1:]:
        ax.plot(x, x**2+10-10*np.cos(2*math.pi*x), 'o-', color='grey')

    plt.legend(loc='upper left')

    # show the plot
    plt.show()
    if save:
        plt.savefig('plot')
