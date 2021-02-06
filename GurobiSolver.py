import Solver
import math

#TO DO : A REVOIR NON FINI

class GurobiSolver(Solver):
    
    def __init__(self):
        pass
    
    def compute(self, file):
        pass
    
    
    def dualCost(self, model : Model):
        #TO DO : Dual Cost
        pass
    
    def valueBoundDifference(self, model : Model):
        return model.cbGet(GRB.Callback.MIPNODE_OBJBND) - model.cbGet(GRB.Callback.MIPNODE_OBJBND)
    
    def valueRootActualNodeDifference(self, root : Model, model : Model):
        return root.cbGet(GRB.Callback.MIPNODE_OBJBND) - model.cbGet(GRB.Callback.MIPNODE_OBJBND)        
    
    def distanceNearestInteger(self, model : Model):
        #ERROR MANAGEMENT
        pass
    
    def distanceNearestUpperInteger(self, model : Model):
        #ERROR MANAGEMENT
        pass
    
    def integralityGap(self, model : Model):
        return math.inf - model.model.cbGet(GRB.Callback.MIPNODE_OBJBND)
    
    
    
    def actualLowerBound(self, model : Model):
        pass
    
    def globalLowerBound(self, model : Model):
        pass
    
    def actualUpperBound(self, model : Model):
        pass
    
    def globalUpperBound(self, model : Model):
        pass
    
    
    
    def lowerCoefficientObjective(self, model : Model):
        pass
    
    def upperCoefficientObjective(self, model : Model):
        pass
    
    
    
    def minDegreeConstraintRoot(self, root : Model):
        pass
    
    def maxDegreeConstraintRoot(self, root : Model):
        pass
    
    def meanDegreeConstraintRoot(self, root : Model):
        pass
    
    def sdDegreeConstraintRoot(self, root : Model):
        pass
    
    
    
    def minVariableImproveRate(self, model : Model):
        pass
    
    def maxVariableImproveRate(self, model : Model):
        pass
    
    def meanVariableImproveRate(self, model : Model):
        pass
    
    def sdVariableImproveRate(self, model : Model):
        pass
    
    def firstQuartileVariableImproveRate(self, model : Model):
        pass    
    
    def thirdQuartileVariableImproveRate(self, model : Model):
        pass
    
    
    
    def minInvSumVariables(self, model : Model):
        pass
    
    def maxInvSumVariables(self, model : Model):
        pass
    
    def meanInvSumVariables(self, model : Model):
        pass
    
    def sdInvSumVariables(self, model : Model):
        pass
    
    def sumInvSumVariables(self, model : Model):
        pass
    
    
    
    def minInvSumVariablesUnfixed(self, model : Model):
        pass
    
    def maxInvSumVariablesUnfixed(self, model : Model):
        pass
    
    def meanInvSumVariablesUnfixed(self, model : Model):
        pass
    
    def sdInvSumVariablesUnfixed(self, model : Model):
        pass
    
    def sumInvSumVariablesUnfixed(self, model : Model):
        pass
    
    
    def minUnitWeight(self, model : Model):
        pass
    
    def maxUnitWeight(self, model : Model):
        pass
    
    def meanUnitWeight(self, model : Model):
        pass
    
    def sdUnitWeight(self, model : Model):
        pass
    
    def sumUnitWeight(self, model : Model):
        pass
    
    
    
    def minDegreeConstraint(self, model : Model):
        pass
    
    def maxDegreeConstraint(self, model : Model):
        pass
    
    def meanDegreeConstraint(self, model : Model):
        pass
    
    def sdDegreeConstraint(self, model : Model):
        pass
    
    
    
    def constraintsNumber(self, model : Model):
        pass
    
    def negativeConstraintsNumber(self, model : Model):
        pass
    
    def positiveConstraintsNumber(self, model : Model):
        pass
    
    
    
    def solutionsNumber(self, model : Model):
        pass
    
    
    
    def coefficientsNumber(self, model : Model):
        pass
    
    def minCoefficient(self, model : Model):
        pass
    
    def maxCoefficient(self, model : Model):
        pass
    
    def meanCoefficient(self, model : Model):
        pass
    
    def sdCoefficient(self, model : Model):
        pass
    
    
    
    def fractionalPart(self, model : Model):
        pass
    
    
    def lowerCoefficientToVariable(self, model : Model):
        pass
    
    def upperCoefficientToVariable(self, model : Model):
        pass    
    
    
    
    def minPositiveCoefficient(self, model : Model):
        pass
    
    def maxPositiveCoefficient(self, model : Model):
        pass
    
    def minNegativeCoefficient(self, model : Model):
        pass
    
    def maxNegativeCoefficient(self, model : Model):
        pass
    
    
    def weightSignedVariable(self, model : Model): #weight of the variable according to its sign
        pass
    
    def weightMinPositiveCoefficent(self, model : Model):
        pass
    
    def weightMaxPositiveCoefficient(self, model : Model):
        pass
    
    def weightMinNegativeCoefficent(self, model : Model):
        pass
    
    def weightMaxNegativeCoefficient(self, model : Model):
        pass
    
    
    
    def depthNode(self, model : Model):
        pass
    
    
    
    def lowerPseudoCost(self, model : Model):
        pass
    
    def upperPseudoCost(self, model : Model):
        pass
    
    def ratioPseudoCosts(self, model : Model):
        pass
    
    def sumPseudoCosts(self, model : Model):
        pass
    
    def productPseudoCosts(self, model : Model):
        pass
    
    
    
    
    
    def UpDriebreekPenalties(self, model :  Model): #TO DO : Search
        pass
    
    def DownDriebreekPenalties(self, model :  Model): #TO DO : Search
        pass    
    
    
    
    
    def estimatedObjectiveValue(self, model :  Model):
        pass
    
    def actualVariableImprovementRate(self, model : Model):
        pass
    
    
    
    def detectedCutsNumber(self, model : Model):
        pass
    
    def lowerBoundAfterCut(self, model : Model):
        pass
    
    def upperBoundAfterCut(self, model : Model):
        pass
        