from typing import List

import Node
import cplex
from cplex.callbacks import ControlCallback


class GatherMIPControllCallback(ControlCallback):
    def __init__(self, env):
        ControlCallback.__init__(self, env)
        self.nodes_list = None
        
    def setNodesList(self, nodes_list: List[Node]):
        self.nodes_list = nodes_list
    
        
    def __call__(self):
        
        #get stats 
        
        self.nodes_list[-1].setId(self.get_node_ID())
        
        pseudo_cost = self.get_pseudo_costs(self.nodes_list[-1].branching_variable)
        
        lowerBoundOfAllVariables = self.get_lower_bounds()
        
        upperBoundOfAllVariables = self.get_upper_bounds()
        
        
        solutionAtNode = self.get_values() #values of solution
        
        
        #set features
        
        self.nodes_list[-1].featuresSet.lower_pseudo_cost = pseudo_cost[0]
        self.nodes_list[-1].featuresSet.upper_pseudo_cost = pseudo_cost[1]