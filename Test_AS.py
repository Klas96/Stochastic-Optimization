import unittest
from AntSystem import AntSystem 


class test_AS(unittest.TestCase):

    def test_AS(self):
        '''
        Test Ant System
        '''
        finalAns, variabel = AntSystem() #Dont look good
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)
        self.assertEqual(finalAns, fitnessFunction(variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{fitnessFunction(variabel)=}")



if __name__ == '__main__':
    unittest.main()