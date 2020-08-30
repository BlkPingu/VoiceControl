from processors.Processor import Processor
from transcribers.BatchTranscriber import BatchTranscriber
from transcribers.StreamTranscriber import StreamTranscriber
from transcribers.MicrophoneTranscriber import MicrophoneTranscriber
from config import conf
from utility.Paths import path_to_base

class Application():

    def __init__(self, processor, transcriber):
        self.processor = processor
        self.transcriber = transcriber

    def run(self, transcriptions):
        self.processor.run(transcriptions)

        out = self.processor.get_results_df()
        print(out)



    def detect_from_source(self):
        """processes input from batch of wav files"""


        if type(self.transcriber) is BatchTranscriber or StreamTranscriber:
            transcriptions = [self.transcriber.transcribe_from(wav=path_to_base(dat)) for dat in conf['audio_wave_path']]
            self.run(transcriptions)
        elif type(self.transcriber) is MicrophoneTranscriber:
            transcriptions = [self.transcriber.transcribe_from()]
            self.run(transcriptions)
