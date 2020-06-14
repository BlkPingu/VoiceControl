import deepspeech
import wave
import numpy as np
import spacy
from config import conf
import pandas as pd

nlp = spacy.load("en_core_web_sm")
model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])


def transcribe(wav):

    filename = wav
    w = wave.open(filename, 'r')
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)
    context = model.createStream()
    buffer_len = len(buffer)
    offset = 0
    batch_size = 16384
    text = ''
    while offset < buffer_len:
        end_offset = offset + batch_size
        chunk = buffer[offset:end_offset]
        data16 = np.frombuffer(chunk, dtype=np.int16)
        model.feedAudioContent(context, data16)
        text = model.intermediateDecode(context)
        print(text)
        offset = end_offset

    text = model.finishStream(context)

    return text


# takes transcribe()
def process(transcription, keyword):
    doc = nlp(transcription)

    texts = [token.text for token in doc]

    if keyword in texts:
        return (transcription, keyword, True)
    else:
        return (transcription, keyword, False)

# takes process()
def to_array(data, cols):

    df = pd.DataFrame.from_records(data, columns = cols)

    return df


def runner():
    keyword = "forward"

    transcriptions = [transcribe(dat) for dat in conf['audio_wave_path']]
    results = [process(transcription, keyword) for transcription in transcriptions]

    table = to_array(results, ['input', 'keyword', 'result'])

    print(table)

def main():
    runner()


if __name__ == "__main__":
    main()