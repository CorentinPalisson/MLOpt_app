from typing import List

import Node
import cplex
from cplex.callbacks import MIPCallback

class GatherMIPInfoCallback(MIPCallback):
    def __init__(self, env):
        MIPCallback.__init__(self, env)
        self.nodes_list: List[Node] = None
        
    def setNodesList(self, nodes_list):
        self.nodes_list = nodes_list
    
    def addNodeToList(self):
        self.nodes_list.append(Node())
        
    def __call__(self):
        
        #get stats
        
        numberRows = get_num_rows()
        coef = self.get_objective_coefficients()
        depth = self.get_current_node_depth()
        
        #set features
        
        self.nodes_list[-1].featuresSet.setConstraintsNumber(numberRows)
    
        self.nodes_list[-1].featuresSet.setLowerCoefficientObjective(min(coeff))
        self.nodes_list[-1].featuresSet.setUpperCoefficientObjective(max(coeff))
        
        self.nodes_list[-1].featuresSet.setDepth(self.get_current_node_depth(depth))
        
        