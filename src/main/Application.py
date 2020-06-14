from processors import Processor
from transcribers.Transcriber import Transcriber
from config import conf

def runner_from_file(Processor:processor, Transcriber:transcriber, str:keyword):

    transcriptions = [transcriber.transcribe(dat) for dat in conf['audio_wave_path']]
    results = [processor.process(transcription, keyword) for transcription in transcriptions]

    table = to_array(results)

    print(table)