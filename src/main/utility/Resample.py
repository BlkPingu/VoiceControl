import librosa
import numpy as np
import soundfile as sf

def resample(path, sr_in):
    rate = 16000
    # Read 16bit PCM WAV
    y, sr = librosa.load(path, sr=sr_in)
    y_16k = librosa.resample(y, sr, rate)
    # Write out audio as 16bit PCM WAV 16kHz
    sf.write(path, y_16k, rate, subtype='PCM_16')

    print('resampled: ' + path)