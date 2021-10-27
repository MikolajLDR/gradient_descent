
import math
import numpy as np

from plots import plot, plot_3d
from gradient_descent import find_minimum

if __name__ == '__main__':
    
    # ---------------- Function G ----------------
    
    function_g = lambda x: [2*x[0]+20*math.pi*math.sin(2*math.pi*x[0])]

    starting_x = 0.4
    learn_rate = 0.0004

    x_points = [x[0] for x in find_minimum(function_g, learn_rate, starting_x)]
    plot_x = np.linspace(-0.1, 0.5, 200)
    function = plot_x**2+10-10*np.cos(2*math.pi*plot_x)
    
    plot(plot_x, x_points, function)
    
    # ---------------- Function F ----------------
    
    function_f = lambda x: [2*x[0], 2*x[1]]
    
    starting_x1 = 300
    starting_x2 = 200
    learn_rate = 0.4
    
    x_y_points = find_minimum(function_f, learn_rate, starting_x1, starting_x2)
    plot_x1 = np.linspace(-310, 310, 50)
    plot_x2 = np.linspace(-310, 310, 50)
    
    x, y = np.meshgrid(plot_x1, plot_x2)
    
    function = x**2 + y**2

    plot_3d(x, y, x_y_points, function)
