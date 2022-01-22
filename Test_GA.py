import unittest
from GeneticAlgorithm.main import GA

class test_GA(unittest.TestCase):

    def test_GA(self):
        finalAns, variabel = GA()
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)



if __name__ == '__main__':
    unittest.main()