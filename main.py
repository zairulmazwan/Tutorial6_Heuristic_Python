import File
import Hill_Climbing as hc

# This main program is complete. Do not need to progress. Run this file for the experiment.
data = File.read_dataset()
hc = hc.Hill_Climbing(data)
hc.run_hc(100)



# ©Zairul Mazwan©