import numpy as np
import random

from .evaluate_individuals import evaluate_individual


def tournament_select(population, pTor = 0.75, torSize = 5):
    '''
    Pre: fitArr vector of fitness values, pTor tournament selection parameter, torSize the tournament size.
    Ret: index Index of the selcted indvidual using tournament selction.
    '''

    popSize = len(population)

    # Chosing torSize individual to participate in tournament
    # TorSize numbers between 0 and popSize
    selected = np.random.randint(popSize,size=torSize)

    fitList = np.array([])
    for i in selected:
        chrom = population[i]
        fitList = np.append(fitList, evaluate_individual(chrom))

    #sort lists
    indexes = np.argsort(fitList)
    fitList = fitList[indexes]
    selected = selected[indexes]

    # Preforme Selection
    for i in range(len(selected)):
        index = selected[i]
        if(random.uniform(0, 1) < pTor):
            break
        else:
            index = selected[i]

    return(population[index])
