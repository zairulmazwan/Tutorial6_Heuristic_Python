
def read_dataset():
    with open("dataset.csv", "r") as file:
        dataset = file.read().split(",")
        dataset = [float(i) for i in dataset]
    return dataset



def write_result(results):

    with open("result.csv","w") as file:
        file.write("Iteration")
        file.write(",")
        file.write("Fitness")
        file.write(",")
        file.write("Solution")
        file.write("\n")

        for i in range(len(results)):
            file.write(str(results[i][0]))
            file.write(",")
            file.write(str(results[i][1]))

            for j in results[i][2]:
                file.write(str(j))
                file.write(",")
            file.write("\n")


# ©Zairul Mazwan©



