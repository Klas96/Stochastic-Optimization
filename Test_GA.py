import unittest
import GeneticAlgorithm.genetic_algorithm as GA


class test_GA(unittest.TestCase):

    def test_GA(self):
        finalAns, variabel = GA.GA() #Dont look good
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)



if __name__ == '__main__':
    unittest.main()