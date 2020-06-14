from Application import runner
from processors.Processor import Processor
from transcribers.BatchTranscriber import BatchTranscriber
from transcribers.StreamingTranscriber import StreamingTranscriber

def main():
    runner_from_file(processor=Processor, transcriber=StreamingTranscriber, keyword="forward")

if __name__ == "__main__":
    main()