from Application import Application
from processors.Processor import Processor
from transcribers.BatchTranscriber import BatchTranscriber
from transcribers.StreamTranscriber import StreamTranscriber
from transcribers.MicrophoneTranscriber import MicrophoneTranscriber

from config import conf


"""
run in DeepSpeech_VirtualEnv/
as python3 voice_control/src/main/main.py
"""

def main():
    processor = Processor()
    transcriber = BatchTranscriber()

    app = Application(processor, transcriber)

    app.detect_from_source(csv=True)

if __name__ == "__main__":
    main()
