import numpy as np
#Function 1 
def read_values_from_file(filename):
   with open(filename, 'r') as file:
       values = [float(line.strip()) for line in file]
   return np.array(values)

arr = read_values_from_file(r"C:\Users\6312999\Downloads\values.txt")
print(arr)


#Function 2


def read_oscillatory_wave_data(filename):
   data = np.loadtxt(filename, delimiter=',')  # Assuming CSV format
   lengths = data[:, 0]
   amplitudes = data[:, 1]
   mean_amplitude = np.mean(amplitudes)
   max_amplitude = np.max(amplitudes)
   return data, mean_amplitude, max_amplitude


data, mean_amp, max_amp = read_oscillatory_wave_data(r"C:\Users\6312999\Downloads\wave_data.csv")
print("mean amplitude:", mean_amp)
print("max amplitude:", max_amp)




#Function 3

def read_standing_wave_data(filename):
   data = np.loadtxt(filename, delimiter=',')  # Assuming CSV format
   lengths = data[:, 0]
   tensions = data[:, 1]
   wave_speeds = np.sqrt(tensions / lengths)  # Assuming μ = 1
   return data, wave_speeds


data, wave_speeds = read_standing_wave_data(r"C:\Users\6312999\Downloads\standing_wave.csv")
print("wave speeds:", wave_speeds)