import unittest
from AntSystem import AntSystem 


def DeBug():
    # Parameters
    
    numberOfAnts = 50  # To do: Set to appropriate value.
    alpha = 1.0        # To do: Set to appropriate value.
    beta = 2.0         # To do: Set to appropriate value.
    rho = 0.7          # To do: set to appropriate value.

    node_positions = [(2,3), (1,3), (4,3)]
    number_of_nodes = len(node_positions)
    nearestNeighbourPathlen = GetNearestNeighbourPathlen(node_positions)
    tau0 = numberOfAnts/nearestNeighbourPathlen
    pheromoneLevel = InitializePheromoneLevels(number_of_nodes, tau0)
    visibility = get_visibility(node_positions)

    path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
    GetPathlen(path,cityLocation)
    GetPathlen(randperm(50),cityLocation)
    GetPathlen(randperm(50),cityLocation)
    GetPathlen(randperm(50),cityLocation)




class test_AS(unittest.TestCase):

    def test_AS(self):
        '''
        Test Ant System
        '''
        finalAns, variabel = AntSystem()
        self.assertIsInstance(finalAns, float)
        self.assertIsInstance(variabel, list)
        self.assertEqual(finalAns, fitnessFunction(variabel))
        
        print(f"{finalAns=}")
        print(f"{variabel=}")
        print(f"{fitnessFunction(variabel)=}")



if __name__ == '__main__':
    unittest.main()