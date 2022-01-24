import unittest
import GeneticAlgorithm.genetic_algorithm as GA
from GeneticAlgorithm.evaluate_individuals import function_to_mimimixe
from GeneticAlgorithm.decode_chromosone import decode_binary_chromosone

'''
python testMyCase.py MyCase.testItIsHot
'''


class test_GA(unittest.TestCase):
    #TODO test other functions
    def test_GA(self):
        '''
        Test Genetic Algorithm
        '''
        finalAns, variabel = GA.GA() #Dont look good
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)
        self.assertEqual(finalAns, function_to_mimimixe(variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{function_to_mimimixe(variabel)=}")

    def test_decode_binary_chromosone(self):
        '''
        Test decode_binary_chromosone
        '''
        varlen = 35
        chrom = [1]*varlen + [0]*varlen
        low_inter = -10
        up_inter = 50
        decode_variable = decode_binary_chromosone(chrom, intrevall = [low_inter, up_inter], varLength = varlen)

        self.assertEqual(up_inter, decode_variable[0])
        self.assertEqual(low_inter, decode_variable[1])

        print(decode_variable)
    
    def target_function(var):
        x1 = var[0]
        x2 = var[1]
        x3 = var[2]

        function_value = (x1-3)**2 + (x2-7)**2 + (x3-1)**2

        return(function_value)
    
    def test_minimize_target_function(self):
        finalAns, variabel = GA.GA(target_function = self.target_function, verbose = True)
        print(f"{finalAns=} , {variabel=}")



if __name__ == '__main__':
    unittest.main()