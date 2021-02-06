from typing import List

import Node
import cplex
from cplex.callbacks import LazyConstraintCallback

class MIPLazyConstraintCallback(LazyConstraintCallback):
    
    def __init__(self, env):
        LazyConstraintCallback.__init__(self, env)
        self.nodes_list: List[Node] = None
        
    def setNodesList(self, nodes_list: List[Node]):
        self.nodes_list = nodes_list
        
    def __call__(self):
        pass
        #callback will be used when CPLEX finds a new integer feasible solution and when CPLEX finds that the LP relaxation at the current node is unbounded.