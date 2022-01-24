from .decode_chromosone import decode_binary_chromosone
import numpy as np

def function_to_mimimixe(var):
    x1 = var[0]
    x2 = var[1]
    x3 = var[2]

    r1 = (x1-0.5)**2
    r2 = (x2-0.5)**2
    r3 = (x3-0.5)**2

    func_value = r1+r2+r3

    if(func_value == 0): func_value = 1e-10

    return(func_value)



def decorator_maximize(fnc):

    def inner(var):
    
        fit_value = fnc(var)
        return(fit_value)
    
    return inner

def target_to_fitness_min(fnc):

    def inner(var):
        func_value = fnc(var)

        if(func_value == 0): func_value = 1e-10

        return(1/func_value)
    
    return inner



def evaluate_individual(chrom, target_function = function_to_mimimixe, minmize = True):
    '''
    Pre: Chromosone
    Ret: Fitness value, The closer to zero the better preformence.
    '''

    if(minmize):
        fitness_function = target_to_fitness_min(target_function)

    var = decode_binary_chromosone(chrom)
    fit_value = fitness_function(var)

    return(fit_value)


@target_to_fitness_min
def fitness_function(var, target_function = function_to_mimimixe):
    '''
    Pre: List of Variables
    Ret: Fitness value

    if minimum max the fitness value
    if maximum min the fitness value

    we are allways trying to maximize fitness value
    '''

    func_value = target_function(var)

    if(func_value == 0): func_value = 1e-10

    return(func_value)





def fitness_function_one(var):
    '''
    Pre: List of Variables
    Ret: Fitness value

    if minimum max the fitness value
    if maximum min the fitness value

    we are allways trying to maximize fitness value
    '''

    x1 = var[0]
    x2 = var[1]
    x3 = var[2]

    r1 = (1+(x1+x2+1)**2*(19 - 14*x1 + 3*x1**2 - 14*x2 + 6*x1*x2 + 3*x2**2))
    r2 = (30 + (2*x1 - 3*x2)**2*(18 - 32*x1 + 12*x1**2 + 48*x2 - 36*x1*x2 + 27*x2**2))

    g = r1*r2

    if(g == 0):
        g = 10**(-10)

    return(1/g)
