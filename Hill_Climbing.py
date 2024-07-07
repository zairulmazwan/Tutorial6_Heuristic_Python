import File
import Scales_Problem as sp
import random as rd

class Hill_Climbing:

    def __init__(self, data):
        self.solution1 = sp.Scales(data)
        self.solution2 = sp.Scales(data)
        self.solution2.copy_solution(self.solution1)


    def small_change(self):
        pass #     complete your code here





    def run_hc(self, iter):

        results = []
        print("Initial solution : ")
        counter = 1
        for i in range(iter):

            row = []
            print("Iter ",i)

            print("New solution: ")
            # complete your code here


            print("Current solution: ")
            # complete your code here


            # if (complete your code here):
            #     complete your code here

            row.append(counter)
            # complete your code here

            results.append(row)
            counter+=1
            print()

        File.write_result(results)








# ©Zairul Mazwan©