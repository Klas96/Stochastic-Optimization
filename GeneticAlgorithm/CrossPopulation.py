import random
import numpy as np
from .TournamentSelection import tournamentSelect


def crossPopulation(population, pCross = 0.8):
    '''
    Pre: popultaion
    Ret: Crossed population
    '''

    crossedPopulation = []
    for i in range(0,len(population),2):
        #Tournament selection
        select1 = tournamentSelect(population)
        select2 = tournamentSelect(population)
        if(random.uniform(0, 1) < pCross):
            #Cross
            child1,child2 = crossChromosones(select1, select2)
        else:
            child1 = select1
            child2 = select2

        crossedPopulation.append(child1)
        crossedPopulation.append(child2)
    #return crossed
    return(crossedPopulation)


def crossChromosones(chrom1,chrom2):
    '''
    Pre: Cross two chromosones with one point crossover
    Ret1: Crossed chromosone
    Ret2: crossed Chromosone
    '''

    lenChrom = chrom1.size
    splitPoint = np.random.randint(0,lenChrom)

    #Spliting
    chrom1Part1 = chrom1[:splitPoint]
    chrom1Part2 = chrom1[splitPoint:]

    chrom2Part1 = chrom2[:splitPoint]
    chrom2Part2 = chrom2[splitPoint:]

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