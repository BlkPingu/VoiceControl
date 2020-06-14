import interfaces.TranscriberInterface
class StreamingTranscriber(interfaces.TranscriberInterface, Transcriber):

    def transcribe_from(wav):
        filename = wav
        w = wave.open(filename, 'r')
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        context = model.createStream()
        buffer_len = len(buffer)
        offset = 0
        batch_size = 16384
        text = ''
        while offset < buffer_len:
            end_offset = offset + batch_size
            chunk = buffer[offset:end_offset]
            data16 = np.frombuffer(chunk, dtype=np.int16)
            model.feedAudioContent(context, data16)
            text = model.intermediateDecode(context)
            print(text)
            offset = end_offset

        text = model.finishStream(context)

        return text