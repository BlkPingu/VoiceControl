from interfaces.TranscriberInterface import TranscriberInterface
from transcribers.Transcriber import Transcriber
import wave
import numpy as np
from utility.Resample import resample

class BatchTranscriber(Transcriber):

    def transcribe_from(self, *args, **kwargs):
        wav = kwargs.get('wav', None)
        w = wave.open(wav, 'r')
        rate = w.getframerate()

        if rate != 16000:
            resample(wav, rate)
            w = wave.open(wav, 'r')

        new_rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        metadata = self.model.sttWithMetadata(data16)

        return metadata