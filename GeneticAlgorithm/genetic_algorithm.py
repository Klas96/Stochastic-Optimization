#from .form_next_generation import form_next_generation
from .initialize_population import initialize_population
from .decode_chromosone import decode_binary_chromosone
from .cross_population import cross_population
from .mutate_population import mutate_population
from .insert_best_individual import insert_chromosone, find_best_chrom
import inspect
import numpy as np
import inspect


#Todo add function as vaiable
#Todo add exit criteria
# TODO make target Function a requiered argument
class GA():

    def __init__(self, target_function, population_size=100, init_range = (0,10), minimize = True, numGenerations = 250, verbose = False):
        self.target_function = target_function
        self.minimize = minimize
        self.numGenerations = numGenerations
        self.verbose = verbose
        self.num_var = len(inspect.signature(target_function).parameters)
        self.population_size = population_size
        self.population = initialize_population(population_size=self.population_size,number_of_variabels = self.num_var, variabel_length = 25)


    def run(self):
        if self.verbose:
            print("Running GA")
            print(f"Number of Generations: {self.numGenerations}")
        

        curent_optima = float('inf')
        if not self.minimize:
            curent_optima = -curent_optima

        #TODO get from population
        curent_best_fitness = -float('inf')

        all_best_variables = []
        
        # Evolve
        for i in range(self.numGenerations):
            
            self.population, best_chrom, max_fitnes = self.form_next_generation()

            # Decode Best Chromsone

            if curent_best_fitness < max_fitnes:
                curent_best_fitness = max_fitnes
                all_best_variables = np.copy(decode_binary_chromosone(best_chrom, num_var = self.num_var))
                curent_optima = self.target_function(*all_best_variables)

            if self.verbose:
                print(f"Generation: {i}, {curent_optima=}, {all_best_variables=}")

        
        return curent_optima, all_best_variables

    def form_next_generation(self):
        '''
        pre: population
        return: population, best_chrom, min_fitness
        '''
        # Build Fittnnes Array
        num_args = len(inspect.signature(self.target_function).parameters)

        # Find current best Chromsome
        # TODO get from parameter
        max_fitness, best_chrom = find_best_chrom(self.population, self.target_function)

        #Cross Population
        self.population = cross_population(self.population, self.target_function)

        # Mutate Poulation
        self.population = mutate_population(self.population)

        # Insert best chromosome
        population = insert_chromosone(best_chrom, self.population)
        
        # Return Next Generation:
        return(self.population, best_chrom, max_fitness)