from processors.Processor import Processor
from transcribers.StreamTranscriber import StreamTranscriber
from config import conf

class Application():

    def __init__(self, processor, transcriber):
        self.processor = processor
        self.transcriber = transcriber


    def detect_detect_batch(self, transcriptions):

        transcriptions = [self.transcriber.transcribe_from(dat) for dat in conf['audio_wave_path']]

        process_keyworld(transcriptions)

        print(self.processor.results_df)


    def detect_from_mic(self):
        transcriptions = [self.transcriber.transcribe_from()]

        process_keyworld(transcriptions)

        print(self.processor.results_df)



    def process_keyword(self, transcriptions):
        results = List()
        for keyword in conf['keywords']:
            result = [self.processor.process(transcription, keyword) for transcription in transcriptions]
            results.append(result)

        data = process_keyword(self.processor, transcriptions)

        df = self.processor.to_df(data, ['input', 'keyword', 'result'])

        self.processor.append(df)