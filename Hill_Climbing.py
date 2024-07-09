import File
import Scales_Problem as sp
import random as rd

class Hill_Climbing:

    def __init__(self, data):
        # An object of hill climbing has 2 solutions of scales problem. Solution 2 is used for searching any better than solution1
        self.solution1 = sp.Scales(data)
        self.solution2 = sp.Scales(data)
        self.solution2.copy_solution(self.solution1) # When we create an object of hill climbing, we copy the solution from 1 so that small change can be done later.


    # The small change function will do a pertubation toward solution 2 so that it becomes a new solution.
    def small_change(self):
        pass #     complete your code here





    def run_hc(self, iter):

        results = [] # We need this to capture the results to a csv file for analysis
        print("Initial solution : ")

        for i in range(iter):
            row = [] # Prepare an empty list to record the result for each iteration.
            print("Iter ",i)

            print("New solution: ")
            # complete your code here


            print("Current solution: ")
            # complete your code here


            # This if statement is used to check whether solution 2 is better than solution 1. If yes, solution 1 will get a copy of the solution from 2.
            # if (complete your code here):
            #     complete your code here

            row.append(i+1) # This variable is used for having the header (iteration #) in our resulting file.
            # complete your code here

            results.append(row)
            print()

        File.write_result(results) # The results are written to a csv file from File.








# ©Zairul Mazwan©