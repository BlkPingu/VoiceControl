from Application import Application
from processors.Processor import Processor
from transcribers.BatchTranscriber import BatchTranscriber
from transcribers.StreamTranscriber import StreamTranscriber
from config import conf


"""
run in DeepSpeech_VirtualEnv/
as python3 voice_control/src/main/main.py
"""

def main():
    processor = Processor()
    transcriber = StreamTranscriber()
    app = Application(processor, transcriber)
    app.runner_from_file(keyword="forward")

if __name__ == "__main__":
    main()