import numpy as np

class Individual():
    def __init__(self, num_var, var_length, range = (0,10)):
        self.num_var = num_var
        self.var_length = var_length
        self.chromosone = np.random.randint(2, size = num_var*var_length)
        self.fitness = None
        self.range = range
        self.variables = self.decode_chromosone()

    def decode_chromosone(self):
        
        diff = self.range[1]-self.range[0]

        # TODO should be calculated from number of variables and length of chromsone
        decode_variable = []
        for i in range(self.num_var):
            pow = -1
            sum = 0
            for j in range(self.var_length):
                sum += self.chromosone[i*self.var_length + j]*2**(pow)
                pow += -1
            decode_variable.append(self.range[0]+diff/(1-2**(-self.var_length))*sum)

        return(decode_variable)


    def mutate(self):
        p_mut = 0.05
        if np.random.uniform(0, 1) < p_mut:
            index = np.random.randint(len(self.chromosone))
            self.chromosone[index] = abs(1 - self.chromosone[index])

    def evaluate_fitness(self, fittnes_function):
        self.decode_chromosone()
        self.fitness = fittnes_function(*self.variables)
    
