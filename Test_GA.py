import unittest
from GeneticAlgorithm.genetic_algorithm import GA
from GeneticAlgorithm.evaluate_individuals import function_to_mimimixe
from GeneticAlgorithm.decode_chromosone import decode_binary_chromosone
from GeneticAlgorithm.form_next_generation import form_next_generation
from GeneticAlgorithm.initialize_population import initialize_population
import numpy as np
'''
python testMyCase.py MyCase.testItIsHot
'''

def target_function(var):
    x1 = var[0]
    x2 = var[1]
    x3 = var[2]

    function_value = (x1-0.3)**2 + (x2-0.7)**2 + (x3-0.1)**2

    return(function_value)


class test_GA(unittest.TestCase):
    #TODO test other functions
    def test_GA(self):
        '''
        Test Genetic Algorithm
        '''
        finalAns, variabel = GA(target_function=target_function).run()
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, np.ndarray)
        self.assertAlmostEqual(finalAns, function_to_mimimixe(variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{function_to_mimimixe(variabel)=}")


    def test_form_next_generation(self):
        population = initialize_population()
        best_chrom = population[0]
        max_fitness = 0
        population, best_chrom, max_fitness = form_next_generation(population, target_function=target_function)
        self.assertIsInstance(population, np.ndarray)
        self.assertIsInstance(best_chrom, np.ndarray)
        self.assertIsInstance(max_fitness, float)
        
        print(f"{population=}")
        print(f"{best_chrom=}")
        print(f"{max_fitness=}")

    def test_decode_binary_chromosone(self):
        '''
        Test decode_binary_chromosone
        '''
        varlen = 35
        chrom = [1]*varlen + [0]*varlen
        low_inter = -10
        up_inter = 50
        decode_variable = decode_binary_chromosone(chrom, intrevall=[low_inter, up_inter], varLength=varlen)

        self.assertEqual(up_inter, decode_variable[0])
        self.assertEqual(low_inter, decode_variable[1])

        print(decode_variable)
    
    def test_minimize_target_function(self):
        finalAns, variabel = GA(target_function=target_function, verbose=True).run()
        print(f"{finalAns=} , {variabel=}")


if __name__ == '__main__':
    unittest.main()
