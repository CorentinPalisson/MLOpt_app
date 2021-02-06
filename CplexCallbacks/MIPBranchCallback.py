from typing import List

import Node
import cplex
from cplex.callbacks import BranchCallback


class MIPBranchCallback(BranchCallback):

    def __init__(self, env):
        BranchCallback.__init__(self, env)
        self.nodesList: List[Node] = None

    def setNodesList(self, nodes_list: List[Node]):
        self.nodesList = nodes_list

    def __call__(self):
        pass
        # get stats

        # get_branch(self, which_branch)
        # get_num_branches(self)
        # is_integer_feasible(self)

        # set features

        # set behaviour

        # make_branch(self, objective_estimate, variables=[], constraints=[], node_data=None)
        # make_cplex_branch(self, which_branch, node_data=None)
        # prune(self)

    def set_behabiour(self):
        pass
