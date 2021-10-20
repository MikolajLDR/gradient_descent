
import math
import numpy as np

from plots import plot
from gradient_descent import find_minimum

if __name__ == '__main__':
    function_g = lambda x: 2*x+20*math.pi*math.sin(2*math.pi*x) 

    starting_x = 0.4
    learn_rate = 0.002

    x_points = find_minimum(function_g, starting_x, learn_rate)
    plot_x = np.linspace(-1/2, 1/2, 200)
    function = plot_x**2+10-10*np.cos(2*math.pi*plot_x)
    
    plot(plot_x, x_points, function)
