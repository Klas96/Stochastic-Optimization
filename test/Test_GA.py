import unittest
from genetic_algorithm import GA
import numpy as np
from genetic_algorithm.individual import Individual
'''
python testMyCase.py MyCase.testItIsHot
'''

def target_function(x1, x2, x3):

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
        self.assertAlmostEqual(finalAns, target_function(*variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{target_function(*variabel)=}")


    def test_form_next_generation(self):
        ga = GA(target_function=target_function)
        population = ga.initialize_population()
        best_chrom = population[0]
        max_fitness = 0
        best_chrom, max_fitness = ga.form_next_generation()
        self.assertIsInstance(ga.population, np.ndarray)
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
        decode_variable = decode_binary_chromosone(chrom, intrevall=[low_inter, up_inter])

        self.assertEqual(up_inter, decode_variable[0])
        self.assertEqual(low_inter, decode_variable[1])

        print(decode_variable)
    
    def test_minimize_target_function(self):
        finalAns, variabel = GA(target_function=target_function, verbose=True).run()
        # Ans should be close to 0
        # variabel should be close to [0.3, 0.7, 0.1]
        print(f"{finalAns=} , {variabel=}")

    def test_individual(self):
        """
        Test Individual
        """
        indi = Individual(2,25,(2,4))
        self.assertIsInstance(indi, Individual)
        self.assertIsInstance(indi.chromosone, np.ndarray)
        self.assertIsInstance(indi.fitness, float)


if __name__ == '__main__':
    unittest.main()
