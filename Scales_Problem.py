import random as rd
import copy as cp


class Scales:
    def __init__(self, data):
        self.data = data
        self.solution = [rd.randint(0,1) for i in range(len(data))]
        self.fitness = 0.00
        self.calculate_fitness()


    def print_solution(self):
        for i in self.solution:
            print (i, end=" ")
        print("\t", self.fitness)


    # Everytime a scales object is created, this function must be called to calculate the fitness value
    def calculate_fitness(self):
        left = 0
        right = 0
        for i in range(len(self.data)):
            if self.solution[i] == 0:
                left += (self.data[i])
            else:
                right += (self.data[i])

        self.fitness = abs(left-right)


    def copy_solution(self, another_scales):
        self.solution = cp.deepcopy(another_scales.solution)
        self.calculate_fitness()




# ©Zairul Mazwan©