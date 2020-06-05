# source https://stackoverflow.com/a/55209505/5476399

# Imports
from scipy.io import wavfile
import scipy.signal as sps

# Your new sampling rate
new_rate = 16000

path = "wav_files/test.wav"

# Read file
sampling_rate, data = wavfile.read(path)

# Resample data
number_of_samples = round(len(data) * float(new_rate) / sampling_rate)
data = sps.resample(data, number_of_samples)