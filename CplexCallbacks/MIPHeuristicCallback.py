from typing import List

import Node
import cplex
from cplex.callbacks import HeuristicCallback


class MIPHeuristicCallback(HeuristicCallback):
    def __init__(self, env):
        HeuristicCallback.__init__(self, env)
        self.nodes_list: List[Node] = None
        
    def __call__(self):
        pass
    #set_bounds(self, *args)
    #set_solution(self, solution, objective_value=None)    
    
    def setNodesList(self, nodesList):
        self.nodesList = nodesList
        
        #setbehavior
        
        
    
    #def heuristic1(self)
    
    #def heuristic2(self)
        
        