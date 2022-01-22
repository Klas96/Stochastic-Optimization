import unittest
import AntSystem.AntSystem 


class test_AS(unittest.TestCase):

    def test_AS(self):
        '''
        Test Genetic Algorithm
        '''
        finalAns, variabel = GA.GA() #Dont look good
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)
        self.assertEqual(finalAns, fitnessFunction(variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{fitnessFunction(variabel)=}")



if __name__ == '__main__':
    unittest.main()