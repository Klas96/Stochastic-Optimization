#from .form_next_generation import form_next_generation
#from .initialize_population import initialize_population
#from .decode_chromosone import decode_binary_chromosone
from .cross_population import cross_population
#from .mutate_population import mutate_population
from .insert_best_individual import insert_chromosone, find_best_chrom
import inspect
import numpy as np
import inspect
from .individual import Individual

def target_to_fitness_min(fnc):

    def inner(var):
        func_value = fnc(*var)

        if(func_value == 0): func_value = 1e-10

        return(1/func_value)
    
    return inner

class GA():
    #Todo add exit criteria
    # TODO make target Function a requiered argument

    def __init__(self, target_function, population_size=100, init_range = (0,10), minimize = True, numGenerations = 250, verbose = False):
        self.target_function = target_function
        self.fittnes_function = target_to_fitness_min(target_function)
        self.range = init_range
        self.var_length = 25
        self.minimize = minimize
        self.numGenerations = numGenerations
        self.verbose = verbose
        self.num_var = len(inspect.signature(target_function).parameters)
        self.population_size = population_size
        self.population = self.initialize_population()


    def run(self):
        if self.verbose:
            print("Running GA")
            print(f"Number of Generations: {self.numGenerations}")
        

        curent_optima = float('inf')
        if not self.minimize:
            curent_optima = -curent_optima

        #TODO get from population
        curent_best_fitness = -float('inf')

        best_variables = []
        
        # Evolve
        for i in range(self.numGenerations):
            
            best_ind, max_fitnes = self.form_next_generation()

            # Decode Best Chromsone

            if curent_best_fitness < max_fitnes:
                curent_best_fitness = max_fitnes
                best_variables = np.copy(best_ind.variables)
                curent_optima = self.target_function(*best_variables)

            if self.verbose:
                print(f"Generation: {i}, {curent_optima=}, {best_variables=}")

        
        return curent_optima, best_variables

    def form_next_generation(self):
        '''
        return: best_chrom, min_fitness
        '''
        # Build Fittnnes Array

        # Find current best Chromsomemax_fitnes
        # TODO get from parameter
        max_fitness, best_chrom = find_best_chrom(self.population, self.target_function)

        #Cross Population
        self.cross_population()

        # Mutate Poulation
        self.mutate_population()

        # Insert best chromosome
        self.population = insert_chromosone(best_chrom, self.population)
        
        # Return Next Generation:
        return(best_chrom, max_fitness)
    
    def initialize_population(self):
        '''
        Pre: Number of Individuals In Populations
        Ret: Population, List of populationSize number of numpy arrays§
        '''

        population = []
        for _ in range(self.population_size):
            population.append(Individual(self.num_var, self.var_length, range = self.range))

        return(population)


    def mutate_population(self):
        '''
        Pre:population
        Ret:mutated population
        '''
        
        for ind in self.population:
            ind.mutate()


    def find_best_chrom(self):
        '''
        arg: population
        ret: max_fitnes, best_chrom
        '''

        max_fitnes = -float('inf')
        best_ind = self.population[0]

        for ind in self.population:
            fitness_value = ind.evaluate_fitness(self.fittnes_function)
            if(fitness_value > max_fitnes):
                max_fitnes = fitness_value
                best_ind = ind

        return(max_fitnes, best_ind)
    
    def cross_population(self):
        '''
        crossed population
        '''

        self.population = cross_population(self.population, self.fittnes_function)
        
        return self.population