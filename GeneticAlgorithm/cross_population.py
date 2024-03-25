import random
import numpy as np

from .selction_methods import tournament_select


def cross_population(population, target_function, pCross = 0.8):
    '''
    Pre: np.array shpe = chromLen, populationSize
    Ret: np.Arary 
    '''

    crossed_population = []

    for i in range(0,len(population),2):

        # Tournament selection
        select1 = tournament_select(population, target_function)
        select2 = tournament_select(population, target_function)

        if(random.uniform(0, 1) < pCross):
            #Cross
            child1, child2 = cross_chromosones(select1, select2)
        else:
            child1 = select1
            child2 = select2

        crossed_population.append(child1)
        crossed_population.append(child2)
    #return crossed
    #TODO find better fix for numpy
    crossed_population = np.array(crossed_population)
    return(crossed_population)


def cross_chromosones(chrom1,chrom2):
    '''
    Pre: Cross two chromosones with one point crossover
    Ret1: Crossed chromosone
    Ret2: crossed Chromosone
    '''

    length_chromosone = chrom1.size
    split_point = np.random.randint(0,length_chromosone)

    #Spliting
    chrom1Part1 = chrom1[:split_point]
    chrom1Part2 = chrom1[split_point:]

    chrom2Part1 = chrom2[:split_point]
    chrom2Part2 = chrom2[split_point:]

    #Merging
    child1 = np.append(chrom1Part1, chrom2Part2)
    child2 = np.append(chrom2Part1, chrom1Part2)

    return(child1,child2)


def crossChromosonesTwoPoint(chrom1,chrom2):    
    '''
    Pre: Cross two chromosones with one point crossover
    Ret1: Crossed chromosone
    Ret2: crossed Chromosone

    TODO: Cross Population with Two point Crossover
    '''
    pass
