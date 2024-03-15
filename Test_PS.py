import unittest
from ParticleSwarm.particel_svarm import ParticleSwarm
from ParticleSwarm.particle import Particle

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
        #minimum x=7 y=4
        opt_pnt, opt_val = ParticleSwarm(0, 10).run_optimization(objective_func)
        
        print(f"{opt_pnt=}")
        print(f"{opt_val=}")

        self.assertEqual(opt_val, objective_func(*opt_pnt))
        

        #print(f"{objective_function(variabel)=}")

    def test_particle(self):

        objective_func = lambda x,y: (x-7)**2 + (y-4)**2

        test_particle = Particle(0, 10)
        test_particle.update_value(objective_func)

        first_value = test_particle.optima

        test_particle.move()
        test_particle.update_value(objective_func)

        second_value = test_particle.optima

        self.assertTrue(second_value <= first_value)
        self.assertEqual(objective_func(*test_particle.varibale_optima), test_particle.optima)
        

if __name__ == '__main__':
    unittest.main()