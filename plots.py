
import matplotlib.pyplot as plt
import numpy as np
import math


def plot(x: list[float], x_points: list[float], function, save: bool = False):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, function, 'y', label='y=2^2+10-10cos(2πx)')

    markersize = 4

    ax.plot(x_points[0], x_points[0]**2+10-10*np.cos(2*math.pi*x_points[0]),
            'o-', color='red', markersize=markersize)
    for x in x_points[1:]:
        ax.plot(x, x**2+10-10*np.cos(2*math.pi*x),
                'o-', color='grey', markersize=markersize)

    plt.legend(loc='upper left')

    plt.show()
    if save:
        plt.savefig('plot')


def plot_3d(x: list[float], y: list[float], x_y_points: list[tuple], function, save: bool = False):
    ax = plt.axes(projection='3d')
    ax.contour3D(x, y, function, 100, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    markersize = 3

    ax.plot(x_y_points[0][0], x_y_points[0][1], x_y_points[0][0]**2 +
            x_y_points[0][1]**2, 'o-', color='red', markersize=markersize)
    for x1, x2 in x_y_points[1:]:
        ax.plot(x1, x2, x1**2+x2**2, 'o-', color='grey', markersize=markersize)

    plt.show()
    if save:
        plt.savefig('plot_3d')
