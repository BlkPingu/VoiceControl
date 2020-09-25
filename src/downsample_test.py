import librosa
import soundfile as sf

rate = 16000

# Read 16bit PCM WAV 44.1kHz
y, sr = librosa.load('test.wav', sr=44100)
y_16k = librosa.resample(y, sr, rate)
print(y.shape, y_16k.shape)

# Write out audio as 16bit PCM WAV 16kHz
sf.write('test.res.wav', y_16k, rate, subtype='PCM_16')