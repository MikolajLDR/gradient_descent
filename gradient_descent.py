
import math


def trunkate(number: float) -> float:
    '''
    Cut off decimal part after four decimal digits
    '''
    return int(number*10000)/10000


def find_minimum(function_gradient, cur_x, rate) -> list[float]:
    print(f'Starting at\nx = {cur_x:.2f}\n')

    iterations = 5000  # Max number of iterations
    x_points = [cur_x]
    i = 0

    while i < iterations:
        prev_x = cur_x
        cur_x -= rate * function_gradient(prev_x)
        if trunkate(prev_x) == trunkate(cur_x):
            break
        i += 1
        print(f'Iteration {i}')
        print(f'x = {cur_x:.4f}\n')
        x_points.append(cur_x)

    print(f'Local min = {cur_x:.4f}')
    return x_points


def find_minimum_vector(function_gradient, cur_x1, cur_x2, rate):
    print(f'Starting at x = ({cur_x1}, {cur_x2})\n')

    iterations = 5000  # Max number of iterations
    x_y_points = [(cur_x1, cur_x2)]
    i = 0

    while i < iterations:
        prev_x1, prev_x2 = cur_x1, cur_x2
        a, b = function_gradient(prev_x1, prev_x2)
        cur_x1 -= a*rate
        cur_x2 -= b*rate
        if trunkate(prev_x1) == trunkate(cur_x1) and trunkate(prev_x2) == trunkate(cur_x2):
            break
        i += 1
        print(f'Iteration {i}')
        print(f'x = ({cur_x1:.4f}, {cur_x2:.4f})\n')
        x_y_points.append((cur_x1, cur_x2))

    print(f'Local min = ({cur_x1:.4f}, {cur_x2:.4f})')
    return x_y_points


if __name__ == '__main__':
    # Gradient of our function
    function_g = lambda x: 2*x+20*math.pi*math.sin(2*math.pi*x)

    starting_x = -1/3
    learn_rate = 0.003

    find_minimum(function_g, starting_x, learn_rate)

    function_f = lambda x1, x2: [2*x1, 2*x2]

    starting_x1 = 5
    starting_x2 = 14
    learn_rate = 0.005

    find_minimum_vector(function_f, starting_x1, starting_x2, learn_rate)
