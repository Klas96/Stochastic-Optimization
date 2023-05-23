import unittest
from ParticleSwarm.particel_svarm import ParticleSwarm
from ParticleSwarm import particle

class test_PS(unittest.TestCase):
    """
    def objective_function(x, y):

        return (x-7)**2 + (y-4)**2
    """

    def test_PS(self):
        '''
        Test Particle Swarm Optimization
        '''

        #minimum x=7 y=4
        objective_func = lambda x,y: (x-7)**2 + (y-4)**2
        opt_pnt, opt_val = ParticleSwarm(0, 10).run_optimization(objective_func)
        
        print(f"{opt_pnt=}")
        print(f"{opt_val=}")

        #self.assertIsInstance(opt_pnt, list)
        #self.assertIsInstance(opt_val, float)
        #self.assertAlmostEqual()
        self.assertEqual(opt_val, objective_func(*opt_pnt))
        

        #print(f"{objective_function(variabel)=}")

    def test_particle(self):
        particle = particle.particle()
        particle.
        pass

if __name__ == '__main__':
    unittest.main()