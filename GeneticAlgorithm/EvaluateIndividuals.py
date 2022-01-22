from .DecodeChromosone import decode_binary_chromosone


def evaluateIndividual(chrom):
    '''
    Pre: Chromosone
    Ret: Fitness value, The closer to zero the better preformence.
    '''
    var = decode_binary_chromosone(chrom)
    fitValue = fitnessFunction(var)

    return(fitValue)



#TODO Decorator function depending on min or max
def decorator_minize(fnc):
    def inner(var):
        fitValue = fnc(var)
        return(1/fitValue)
    return inner


@decorator_minize
def fitnessFunction(var):
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

    r1 = (x1-0.5)**2
    r2 = (x2-0.5)**2
    r3 = (x3-0.5)**2

    func_value = r1+r2+r3

    if(func_value == 0):
        g = 10**(-10)

    return(func_value)


def fitnessFunctionOne(var):
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

    fitValue = 1/g

    return(fitValue)
