from typing import List

import Node
from cplex.callbacks import NodeCallback

import math

class MIPNodeCallback(NodeCallback):
    
    def __init__(self,env):
        NodeCallback.__init__(self, env)
        self.nodes_list: List[Node] = None
        
    def setNodesList(self, nodes_list: List[Node]):
        self.nodes_list = nodes_list
        
    def __call__(self):
        
        # get features
        
        branching_var = self.get_branch_variable(self.nodes_list[-1].ID)
        integer_and_fractional_part = math.modf(self.get_objective_coefficients(branching_var))
        fractional_part = integer_and_fractional_part[0]
        integer_part = integer_and_fractional_part[1]
        distance_nearest_integer = min(fractional_part, 1-fractional_part)
        distance_nearest_upper_integer = (fractional_part != 0 if 1-fractional_part else fractional_part)
        
        
        #set features
        
        self.nodes_list[-1].setBranchingVariable(branching_var)
        
        self.nodes_list[-1].featuresSet.setEstimatedObjectiveValue(self.get_estimated_objective_value(self.nodes_list[-1].ID))
        
        self.nodes_list[-1].featuresSet.setFractionalPart(fractional_part)
        self.nodes_list[-1].featuresSet.setdistanceNearestInteger(distance_nearest_integer)
        self.nodes_list[-1].featuresSet.setdistanceNearestUpperInteger(distance_nearest_upper_integer)
        