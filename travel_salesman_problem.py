from copy import deepcopy
from random import choice, randint

from cifo.problem.problem_template import ProblemTemplate
from cifo.problem.objective import ProblemObjective
from cifo.problem.solution import LinearSolution, Encoding

tsp_encoding_rule = {
    "Size"         : -1, # It must be defined by the size of DV (Number of products)
    "Is ordered"   : True,
    "Can repeat"   : False,
    "Data"         : [0,0], # must be defined by the data
    "Data Type"    : "Choices"
}
#===================================================================================================
tsp_decision_variables_example = {
    "Distances" : [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0]
    ]
}
#==================================================================================================
# REMARK: There is no constraint

# -------------------------------------------------------------------------------------------------
# TSP - Travel Salesman Problem
# -------------------------------------------------------------------------------------------------
class TravelSalesmanProblem( ProblemTemplate ):
    """
    """

    # Constructor
    #----------------------------------------------------------------------------------------------
    def __init__(self, decision_variables, constraints , encoding_rule = tsp_encoding_rule):
        """
        """
        # optimize the access to the decision variables
        self._distances = []
        if "Distances" in decision_variables:
            self._distances = decision_variables["Distances"]

        encoding_rule["Size"] = len(self._distances)
        # Call the Parent-class constructor to store these values and to execute  any other logic to be implemented by the constructor of the super-class
        super().__init__(
            decision_variables = decision_variables,
            constraints = constraints,
            encoding_rule = encoding_rule
        )

        #========================================================
        self._encoding.encoding_data = []
        if "Data" in encoding_rule:
            self._encoding.encoding_data = [city for city in range(len(self._distances))]

        encoding_rule["Data"] = self._encoding.encoding_data
        #========================================================

        # 1. Define the Name of the Problem
        self._name = "Travel Salesman Problem"
        
        # 2. Define the Problem Objective
        self._objective = ProblemObjective.Minimization

    # Build Solution for Travel Salesman Problem
    #----------------------------------------------------------------------------------------------
    def build_solution(self):
        """
        """
        solution_representation = []
        encoding_data = deepcopy(self._encoding.encoding_data)

        while len(solution_representation) < self._encoding.size:
            new_city = choice(encoding_data)
            encoding_data.remove(new_city)
            solution_representation.append(new_city)

        solution = LinearSolution(
            representation = solution_representation, 
            encoding_rule = self._encoding_rule
        )
        
        return solution

    # Solution Admissibility Function - is_admissible()
    #----------------------------------------------------------------------------------------------
    def is_admissible( self, solution ): #<< use this signature in the sub classes, the meta-heuristic 
        """
        """
        return True

    # Evaluate_solution()
    #-------------------------------------------------------------------------------------------------------------
    # It should be seen as an abstract method 
    def evaluate_solution(self, solution, feedback = None):# << This method does not need to be extended, it already automated solutions evaluation, for Single-Objective and for Multi-Objective
        """
        """
        distances = self._distances
        
        fitness = 0
        
        for city in range(len(solution.representation) - 1):
            fitness += distances[solution.representation[city]][solution.representation[city + 1]]
        
        fitness += distances[solution.representation[-1]][solution.representation[0]]

        solution.fitness = fitness

        return solution    


# -------------------------------------------------------------------------------------------------
# OPTIONAL - it only is needed if you will implement Local Search Methods
#            (Hill Climbing and Simulated Annealing)
# -------------------------------------------------------------------------------------------------
def pip_bitflip_get_neighbors( solution, problem, neighborhood_size = 0 ):
    """
    """
    pass
