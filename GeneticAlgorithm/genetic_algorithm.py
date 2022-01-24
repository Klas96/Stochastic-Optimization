from .form_next_generation import form_next_generation
from .evaluate_individuals import function_to_mimimixe
from .initialize_population import initialize_population
from .decode_chromosone import decode_binary_chromosone

class genetic_algorithm_instanc():
    def __init__():
        pass


#Todo add function as vaiable
#Todo add exit criteria
# TODO make target Function a requiered argument
def GA(target_function = None, minimize = True, numGenerations = 250, verbose = False):
    '''
    arg numGenerations = 250
    verbose = False

    finding 
    '''

    if verbose:
        print("Running GA")
        print(f"Number of Generations: {numGenerations}")
    
    population = initialize_population()

    curent_optima = float('inf')
    if not minimize:
        curent_optima = -curent_optima

    curent_best_fitness = -float('inf')

    curent_best_variables = []
    
    # Evolve
    for i in range(numGenerations):
        
        population, best_chrom, max_fitnes = form_next_generation(population, target_function = target_function)

        # Decode Best Chromsone
        curent_best_variables = decode_binary_chromosone(best_chrom)

        if curent_best_fitness < max_fitnes:
            curent_best_fitness = max_fitnes
            curent_best_variables = decode_binary_chromosone(best_chrom)
            #TODO change to value of real function
            curent_optima = function(curent_best_variables)

        if verbose:
            print(f"Generation: {i}, {curent_optima=}, {curent_best_variables=}")

    
    return curent_optima, curent_best_variables
