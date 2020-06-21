from processors.Processor import Processor

class Application():

    def __init__(self, processor, transcriber):
        self.processor = processor
        self.transcriber = transcriber


    def detect_detect_batch(self):
        """processes input from batch of wav files"""
        transcriptions = [self.transcriber.transcribe_from(dat) for dat in conf['audio_wave_path']]

        self.processor.run(transcriptions)

        out = self.processor.get_results_df()
        print(out)


    def detect_from_mic(self):
        """processes input from microphone"""
        transcriptions = [self.transcriber.transcribe_from()]

        self.processor.run(transcriptions)

        out = self.processor.get_results_df()
        print(out)



