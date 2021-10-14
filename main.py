
import math

def find_minimum(function_gradient, cur_x, rate):
    print(f'Starting at x = {cur_x}\n')
    precision = 0.000001 # When to stop
    prev_step_size = 1
    iterations = 10000 # Max number of iterations

    i = 0
    while (prev_step_size > precision and i < iterations):
        prev_x = cur_x
        cur_x = cur_x - rate * function_gradient(prev_x)
        prev_step_size = abs(cur_x - prev_x)
        i += 1
        print(f'Iteration {i}')
        print(f'x = {cur_x}\n')
    
    print(f'Local min = {cur_x:.3}')
    
if __name__ == '__main__':
    # Gradient of our function
    function_g = lambda x: 2*x+20*math.pi*math.sin(2*math.pi*x) 
    
    starting_x = -8
    learn_rate = 0.003
    
    find_minimum(function_g, starting_x, learn_rate)
    