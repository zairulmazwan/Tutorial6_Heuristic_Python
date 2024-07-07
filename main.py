import File
import Hill_Climbing as hc


data = File.read_dataset()
hc = hc.Hill_Climbing(data)
hc.run_hc(100)



# ©Zairul Mazwan©