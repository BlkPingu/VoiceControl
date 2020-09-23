from processors.Processor import Processor
from transcribers.BatchTranscriber import BatchTranscriber
from transcribers.StreamTranscriber import StreamTranscriber
from transcribers.MicrophoneTranscriber import MicrophoneTranscriber
from config import conf
from utility.Paths import path_to_base
import pandas as pd

class Application():

    def __init__(self, processor, transcriber):
        self.processor = processor
        self.transcriber = transcriber



    def print_results(self):
        out = self.processor.get_results_df()
        print(out)



    def detect_from_source(self, *args, **kwargs):
        """processes input from batch of wav files"""

        if type(self.transcriber) is BatchTranscriber or StreamTranscriber:
            if kwargs.get('csv', False):

                data = pd.read_csv(conf['csv_path'])

                data['TRANSCRIPTION'] = data['PATH'].apply (lambda row: self.transcriber.transcribe_from(wav=row))
                self.processor.run(data, csv=True)

            else:
                transcriptions = [self.transcriber.transcribe_from(wav=path_to_base(dat)) for dat in conf['audio_wave_path']]
                transcription_df = self.to_df(transcriptions, ['transcriptions'])
                self.processor.run(transcription_df)

        elif type(self.transcriber) is MicrophoneTranscriber:
            transcriptions = [self.transcriber.transcribe_from()]
            self.processor.run(transcriptions)






