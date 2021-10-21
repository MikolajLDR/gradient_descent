
import math
import numpy as np

from plots import plot, plot_3d
from gradient_descent import find_minimum, find_minimum_vector

if __name__ == '__main__':
    # ---------------- Function G ----------------
    
    function_g = lambda x: 2*x+20*math.pi*math.sin(2*math.pi*x) 

    starting_x = 0.4
    learn_rate = 0.0025

    max_range = starting_x+(starting_x*0.1)

    x_points = find_minimum(function_g, starting_x, learn_rate)
    plot_x = np.linspace(-max_range, max_range, 200)
    function = plot_x**2+10-10*np.cos(2*math.pi*plot_x)
    
    plot(plot_x, x_points, function, save=True)
    
    # ---------------- Function F ----------------
    
    '''function_f = lambda x1, x2: [2*x1, 2*x2]
    
    starting_x1 = 3
    starting_x2 = 2
    learn_rate = 0.2
    
    if starting_x1 > starting_x2:
        max_range = starting_x1
    else:
        max_range = starting_x2

    max_range += 1
    
    x_y_points = find_minimum_vector(function_f, starting_x1, starting_x2, learn_rate)
    plot_x1 = np.linspace(-max_range, max_range, 50)
    plot_x2 = np.linspace(-max_range, max_range, 50)
    
    x, y = np.meshgrid(plot_x1, plot_x2)
    
    function = x**2 + y**2

    plot_3d(x, y, x_y_points, function, save=True)'''
