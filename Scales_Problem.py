import random as rd
import copy as cp


class Scales:
    def __init__(self, data):
        self.data = data
        # Binary numbers are used for the solution representation for the problem. The data structure is list
        self.solution = [rd.randint(0,1) for i in range(len(data))]
        self.fitness = 0.00
        self.calculate_fitness() # This function is required so that the fitness variable is updated.


    def print_solution(self):
        for i in self.solution:
            print (i, end=" ")
        print("\t", self.fitness)


    # Everytime a scales object is created, this function must be called to calculate the fitness value
    def calculate_fitness(self):
        left = 0
        right = 0
        #     complete your code here

    # This function is used in Hill Climbing for small change.
    def copy_solution(self, another_scales):
        self.solution = cp.deepcopy(another_scales.solution)
        self.calculate_fitness()




# ©Zairul Mazwan©