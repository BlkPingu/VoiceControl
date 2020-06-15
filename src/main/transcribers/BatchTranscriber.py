from interfaces.TranscriberInterface import TranscriberInterface
from transcribers.Transcriber import Transcriber
import wave
import numpy as np

class BatchTranscriber(Transcriber):

    def transcribe_from(self, *args, **kwargs):
        wav = kwargs.get('wav', None)
        w = wave.open(wav, 'r')
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        text = self.model.stt(data16)

        return text
