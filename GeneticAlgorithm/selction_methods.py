import numpy as np
import random
from .evaluate_individuals import evaluate_individual


def tournament_select(population, target_function, pTor = 0.75, torSize = 5):
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
        fitList = np.append(fitList, evaluate_individual(chrom,  target_function))

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


import random

import random

def roulette_wheel_select(population, target_function):
    """
    Performs selection using roulette wheel selection method.

    Args:
    - population (list): A list of individuals.

    Returns:
    - selected_individual: The selected individual.
    """

    # Evaluate fitness scores for all individuals in the population
    fitness_scores = [evaluate_individual(individual,  target_function) for individual in population]

    # Total fitness score
    total_fitness = sum(fitness_scores)

    # Generate a random number between 0 and the total fitness score
    random_number = random.uniform(0, total_fitness)

    # Initialize variables for tracking cumulative fitness score and selected individual
    cumulative_fitness = 0
    selected_individual = None

    # Iterate through individuals and select one based on roulette wheel selection
    for individual, fitness in zip(population, fitness_scores):
        cumulative_fitness += fitness
        if cumulative_fitness >= random_number:
            selected_individual = individual
            break

    return selected_individual
