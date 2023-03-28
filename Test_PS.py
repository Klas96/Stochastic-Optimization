import unittest
from ParticleSwarm.particel_svarm import ParticleSwarm

class test_PS(unittest.TestCase):
    """
    def objective_function(x, y):

        return (x-7)**2 + (y-4)**2
    """

    def test_PS(self):
        '''
        Test Particle Swarm Optimization
        '''

        objective_func = lambda x,y: (x-7)**2 + (y-4)**2
        opt_pnt, opt_val = ParticleSwarm(0, 10).run_optimization(objective_func)

        self.assertIsInstance(opt_pnt, list)
        self.assertIsInstance(opt_val, float)
        #self.assertAlmostEqual()
        #self.assertEqual(finalAns, objective_function(*opt_pnt))
        
        print(f"{opt_pnt=}")
        print(f"{opt_val=}")
        #print(f"{objective_function(variabel)=}")



if __name__ == '__main__':
    unittest.main()