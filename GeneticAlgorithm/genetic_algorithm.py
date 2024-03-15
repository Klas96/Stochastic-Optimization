from .form_next_generation import form_next_generation
from .evaluate_individuals import function_to_mimimixe
from .initialize_population import initialize_population
from .decode_chromosone import decode_binary_chromosone
import numpy as np


#Todo add function as vaiable
#Todo add exit criteria
# TODO make target Function a requiered argument
class GA():


    def __init__(self, target_function, init_range = (0,1), minimize = True, numGenerations = 250, verbose = False):
        self.target_function = target_function
        self.minimize = minimize
        self.numGenerations = numGenerations
        self.verbose = verbose
        self.population = initialize_population(number_of_variabels = 2, variabel_length = 25)


    def run(self):
        if self.verbose:
            print("Running GA")
            print(f"Number of Generations: {self.numGenerations}")
        

        curent_optima = float('inf')
        if not self.minimize:
            curent_optima = -curent_optima

        curent_best_fitness = -float('inf')

        all_best_variables = []
        
        # Evolve
        for i in range(self.numGenerations):
            
            self.population, best_chrom, max_fitnes = form_next_generation(self.population, target_function=self.target_function)

            # Decode Best Chromsone

            if curent_best_fitness < max_fitnes:
                curent_best_fitness = max_fitnes
                all_best_variables = np.copy(decode_binary_chromosone(best_chrom))
                #TODO change to value of real function
                curent_optima = self.target_function(all_best_variables)

            if self.verbose:
                print(f"Generation: {i}, {curent_optima=}, {all_best_variables=}")

        
        return curent_optima, all_best_variables
