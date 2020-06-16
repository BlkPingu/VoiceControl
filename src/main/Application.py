from processors.Processor import Processor
from transcribers.StreamTranscriber import StreamTranscriber
from config import conf

class Application():

    def __init__(self, processor, transcriber):
        self.processor = processor
        self.transcriber = transcriber

    def runner_from_file(self, keyword):

        transcriptions = [self.transcriber.transcribe_from(dat) for dat in conf['audio_wave_path']]
        results = [self.processor.process(transcription, keyword) for transcription in transcriptions]

        return results

    def runner_from_mic(self, keyword):
        transcriptions = [self.transcriber.transcribe_from()]
        results = [self.processor.process(transcription, keyword) for transcription in transcriptions]

        return results

    def print_results(self,results):
        table = self.processor.to_array(results, ['input', 'keyword', 'result'])
        print(table)