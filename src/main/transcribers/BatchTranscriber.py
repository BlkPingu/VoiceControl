import interfaces.TranscriberInterface

class BatchTranscriber(interfaces.TranscriberInterface, Transcriber):

    def transcribe_from(wav):
        w = wave.open(wav, 'r')
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        text = model.stt(data16)
        return text
