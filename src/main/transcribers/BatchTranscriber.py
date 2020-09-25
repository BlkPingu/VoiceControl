from interfaces.TranscriberInterface import TranscriberInterface
from transcribers.Transcriber import Transcriber
import wave
import numpy as np
from utility.Resample import resample

class BatchTranscriber(Transcriber):

    def transcribe_from(self, *args, **kwargs):
        wav_path = kwargs.get('wav', None)
        w = wave.open(wav_path, 'r')
        rate = w.getframerate()

        if rate != 16000 and rate > 0:
            resample(wav_path, rate)
            w = wave.open(wav_path, 'r')
        else:
            print('Good' + wav_path)

        new_rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        metadata = self.model.sttWithMetadata(data16)

        return metadata