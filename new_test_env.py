from cifo.custom_problem.travel_salesman_problem import (
    TravelSalesmanProblem, tsp_decision_variables_example, tsp_encoding_rule)

from cifo.algorithm.ga_operators import (RouletteWheelSelection, initialize_randomly, swap_mutation,  single_point_mutation, cycle_crossover)


tsp1 = TravelSalesmanProblem(tsp_decision_variables_example, {}, tsp_encoding_rule)
s1 = tsp1.build_solution()
if tsp1.is_admissible(s1):
    tsp1.evaluate_solution(s1)
print(s1)

print("SOLUTION REP ", s1.representation)

test_pop1 = initialize_randomly(tsp1, 10)

for solution in test_pop1.solutions:
    print(solution)

rw = RouletteWheelSelection()
rw1 = rw.select(test_pop1, tsp1._objective,'')

print("=========================================== Roulette Wheel Selection ===================================")
print('{', rw1[0], '}')
print('{', rw1[1], '}')

#swpm1 = swap_mutation(tsp1, rw1[0])

#print("=========================================== Swap Mutation ===================================")
#print(swpm1)

cc1 = cycle_crossover(tsp1, rw1[0], rw1[1])

print("=========================================== Cycle Crossover ===================================")
print('{', cc1[0], '}', ' and ', '{', cc1[1], '}')
