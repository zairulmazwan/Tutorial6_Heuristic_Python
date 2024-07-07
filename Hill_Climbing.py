import File
import Scales_Problem as sp
import random as rd

class Hill_Climbing:

    def __init__(self, data):
        self.solution1 = sp.Scales(data)
        self.solution2 = sp.Scales(data)
        self.solution2.copy_solution(self.solution1)


    def small_change(self):
        rd.seed()

        for i in range(2):
            j = rd.randint(0,len(self.solution2.solution)-1)
            if self.solution2.solution[j] == 0:
                self.solution2.solution[j] = 1
            else:
                self.solution2.solution[j] = 0
        self.solution2.calculate_fitness()


    def small_change2(self):
        rd.seed()
        random_index = []

        for i in range(2):
            index = rd.randint(0, len(self.solution2.solution)-1)
            # print("a: ",index)

            while(index in random_index):
                index = rd.randint(0, len(self.solution2.solution) - 1)
                # print("b: ",index)

            if self.solution2.solution[index] == 0:
                self.solution2.solution[index] = 1
            else:
                self.solution2.solution[index] = 0

            random_index.append(index)
        self.solution2.calculate_fitness()



    def run_hc(self, iter):

        results = []
        print("Initial solution : ")
        self.solution1.print_solution()

        counter = 1
        for i in range(iter):

            row = []
            print("Iter ",i)
            self.small_change2()
            print("New solution: ")
            self.solution2.print_solution()
            print(self.solution2.fitness)

            print("Current solution: ")
            self.solution1.print_solution()
            print(self.solution1.fitness)


            if self.solution2.fitness < self.solution1.fitness:
                self.solution1.copy_solution(self.solution2)

            row.append(counter)
            row.append(self.solution1.fitness)
            row.append(self.solution1.solution)
            results.append(row)
            counter+=1
            print()

        File.write_result(results)


    def print_results(self, results):
        counter = 0
        for row in results:
            print(counter)
            print(row)
            counter+=1












# ©Zairul Mazwan©