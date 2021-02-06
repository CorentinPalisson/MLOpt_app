import sys
import CplexSolver
import GurobiSolver

class Resolution:
    
    #Singleton
    class __Resolution:
        def __init__(self, file):
            self.file = file
            self.solver = None
            
    instance = None
    def __init__(self, file):
        if not Resolution.instance:
            Resolution.instance = Resolution.__Resolution(file)
        else:
            Resolution.instance.file = file
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    
    
    def run(self):
        Resolution.instance.solver.compute(file) 
        
    def setSolver(self):
        self.solver = CplexSolver()  #Cplex par defaut / A changer
    
    def print(self):
        pass
        #add print solution
    
        