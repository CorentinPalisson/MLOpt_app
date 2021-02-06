import Solver
import math


class CplexSolver(Solver):
    
    def __init__(self):
        # "If you wish to associate additional data with your callback class, you may do so after it has been registered with the Cplex object."
        self.nodeList = []
        
    def compute(self, file):  # TODO : Create model with file, register callback, solve
        pass
        #get_sense(self)
        
