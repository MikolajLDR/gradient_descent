
import math


def trunkate(number: float) -> float:
    '''
    Cut off decimal part after four decimal digits
    '''
    return int(number*10000)/10000


def stop_condition(prev_xs: tuple, cur_xs: tuple) -> bool:
    '''
    Return False if any xs are equal with approximation
    to 4 decimal places. Otherwise, return True.
    '''
    for prev_x, cur_x in zip(prev_xs, cur_xs):
        if trunkate(prev_x) != trunkate(cur_x):
            return False
    return True


def make_printable_xs(xs) -> str:
    if len(xs) == 1:
        return f'{xs[0]:.4f}'
    else:
        string = '('
        for x in xs:
            string += f'{x:.4f}, '
        string = string[:-2] + ')'
        return string


def find_minimum(function_gradient, rate, *cur_xs) -> list:
    '''
    Find function's local minium with Gradient Descent algorithm.
    Return list with all points.
    '''
    cur_xs = list(cur_xs)
    print(f'Starting at\n{make_printable_xs(cur_xs)}')
    
    iterations = 5000  # Max number of iterations
    x_points = [list(cur_xs)]
    i = 0

    while i < iterations:
        prev_xs = list(cur_xs)
        result = function_gradient(prev_xs)
        for j, a in enumerate(result):
            cur_xs[j] -= a*rate
        if stop_condition(prev_xs, cur_xs):
            break
        i += 1
        print(f'Iteration {i}\n {make_printable_xs(cur_xs)}')
        x_points.append(list(cur_xs))

    print(f'Local min = {make_printable_xs(cur_xs)}')
    return x_points
