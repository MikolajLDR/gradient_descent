
import math


def trunkate(number: float) -> float:
    '''
    Cut off decimal part after two decimal digits
    '''
    return int(number*100)/100

def find_minimum(function_gradient, cur_x, rate) -> list[float]:
    print(f'Starting at\nx = {cur_x:.2f}\n')
    iterations = 5000 # Max number of iterations
    x_points = [cur_x]
    i = 0
    while (i < iterations):
        prev_x = cur_x
        cur_x -= rate * function_gradient(prev_x)
        if trunkate(prev_x) == trunkate(cur_x):
            break
        i += 1
        print(f'Iteration {i}')
        print(f'x = {cur_x:.2f}\n')
        x_points.append(cur_x)
    
    print(f'Local min = {cur_x:.2f}')
    return x_points


def find_minimum_vector(function_gradient, cur_x1, cur_x2, rate):
    print(f'Starting at x = ({cur_x1}, {cur_x2})\n')
    precision = 0.001 # When to stop
    prev_step_size = 1
    iterations = 5000 # Max number of iterations
    x_points = [(cur_x1, cur_x2)]
    i = 0
    while i < iterations and prev_step_size > precision:
        prev_x1, prev_x2 = cur_x1, cur_x2
        a, b = function_gradient(prev_x1, prev_x2)
        cur_x1 -= a*rate
        cur_x2 -= b*rate
        prev_step_size = math.sqrt(math.pow(cur_x1-prev_x1, 2) + math.pow(cur_x2-prev_x2, 2))
        i += 1
        print(f'Iteration {i}')
        print(f'x = ({cur_x1:.2f}, {cur_x2:.2f})\n')
        x_points.append((cur_x1, cur_x2))
    
    print(f'Local min = ({cur_x1:.2f}, {cur_x2:.2f})')


if __name__ == '__main__':
    # Gradient of our function
    function_g = lambda x: 2*x+20*math.pi*math.sin(2*math.pi*x) 
    
    starting_x = -1/3
    learn_rate = 0.003
    
    find_minimum(function_g, starting_x, learn_rate)
    
    #function_f = lambda x1, x2: [2*x1, 2*x2]
    
    #starting_x1 = 5
    #starting_x2 = 14
    #learn_rate = 0.005
    
    #find_minimum_vector(function_f, starting_x1, starting_x2, learn_rate)
