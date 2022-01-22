import unittest
import GeneticAlgorithm.genetic_algorithm as GA
from GeneticAlgorithm.EvaluateIndividuals import fitnessFunction
from GeneticAlgorithm.DecodeChromosone import decode_binary_chromosone

'''
python testMyCase.py MyCase.testItIsHot
'''


class test_GA(unittest.TestCase):

    def test_GA(self):
        '''
        Test Genetic Algorithm
        '''
        finalAns, variabel = GA.GA(verbose = True) #Dont look good
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)
        self.assertEqual(finalAns, fitnessFunction(variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{fitnessFunction(variabel)=}")

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


if __name__ == '__main__':
    unittest.main()