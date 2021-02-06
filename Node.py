from FeaturesSet import FeaturesSet


class Node:
    def __init__(self, model: Model, father):
        self.model = model
        self.father = father
        self.featuresSet = FeaturesSet()
        self.children = []
        
        self.ID = None
        self.branching_variable = None
        
    def compute_features(self, model, solver):
        self.featuresSet.compute_all(model, solver)
    
    def add_child(self, child):
        self.children.append(child)

    def write_into_csv(self):
        pass

        