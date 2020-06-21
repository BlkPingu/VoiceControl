from transcribers.Transcriber import Transcriber
import wave
import numpy as np



class StreamTranscriber(Transcriber):

    def transcribe_from(self, *args, **kwargs):
        wav = kwargs.get('wav', None)
        filename = wav
        w = wave.open(filename, 'r')
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        context = self.model.createStream()
        buffer_len = len(buffer)
        offset = 0
        batch_size = 16384
        text = ''
        while offset < buffer_len:
            end_offset = offset + batch_size
            chunk = buffer[offset:end_offset]
            data16 = np.frombuffer(chunk, dtype=np.int16)
            self.model.feedAudioContent(context, data16)
            text = self.model.intermediateDecode(context)
            print(text)
            offset = end_offset

        metadata = self.model.finishStreamWithMetadata(context)

        return metadata