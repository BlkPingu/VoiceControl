from interfaces.TranscriberInterface import TranscriberInterface
from transcribers.Transcriber import Transcriber
import wave
import numpy as np
import speech_recognition as sr


class MicrophoneTranscriber(Transcriber):

    def transcribe_from(self, *args, **kwargs):
        text = ''
        sample_rate=16000
        r = sr.Recognizer(language = "en-US")
        with sr.Microphone(sample_rate=sample_rate) as source:

            r.adjust_for_ambient_noise(source)

            print("Say Something")
            audio = r.listen(source,timeout=1, phrase_time_limit=4)

            fs = audio.sample_rate
            audio = np.frombuffer(audio.frame_data, np.int16)
            metadata = self.model.sttWithMetadata(audio)
            return metadata

