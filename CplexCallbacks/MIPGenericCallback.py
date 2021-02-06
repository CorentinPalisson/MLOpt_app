from typing import List

import cplex
from cplex.callbacks import Context

import Node


class MIPGenericCallback():
    
    def __init__(self, nodes_list: List[Node]):
        self.nodes_list = nodes_list
        
    def computeFeatures(self, context):
        pass
        
    
    def selectHeuristic(self, context):
        pass
    
    def selectCut(self,context):
        pass
    
    def applyHeuristic(self, context):
        pass
    
    def applyCut(self, context):
        pass
    
    def selectBranching(self,context):
        pass
    
    def invoke(self, context):
        try:
            if context.in_local_progress():
                pass
            elif context.in_global_progress():
                pass
            elif context.in_candidate(): #when new solution is found
                pass
            elif context.in_relaxation(): #when it has found a relaxed solution available
                pass
                #heuristic / cut
            elif context.in_branching(): #when it is done processing a node and has to decide how to branch
                pass
        except Exception as error:
            print(str(error))

        
        
    
    