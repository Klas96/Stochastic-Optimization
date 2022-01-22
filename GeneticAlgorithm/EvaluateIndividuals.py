from .DecodeChromosone import decodeBinaryChromosone


def evaluateIndividual(chrom):
    '''
    Pre: Chromosone
    Ret: Fitness value, The closer to zero the better preformence.
    '''
    var = decodeBinaryChromosone(chrom)
    fitValue = fitnessFunction(var)
    return(fitValue)


def fitnessFunction(var):
    '''
    Pre: List of Variables
    Ret: Fitness value

    if minimum max the fitness value
    if maximum min the fitness value
    '''

    x1 = var[0]
    x2 = var[1]

    r1 = (1+(x1+x2+1)**2*(19 - 14*x1 + 3*x1**2 - 14*x2 + 6*x1*x2 + 3*x2**2))
    r2 = (30 + (2*x1 - 3*x2)**2*(18 - 32*x1 + 12*x1**2 + 48*x2 - 36*x1*x2 + 27*x2**2))

    g = r1*r2

    if(g == 0):
        g = 10**(-10)

    fitValue = 1./g
    return(fitValue)
