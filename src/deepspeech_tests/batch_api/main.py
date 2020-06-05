import deepspeech
from config import conf
import wave
import numpy as np
import spacy


# Run in Bachelorarbeit/Code/DeepSpeech_VirtualEnv:
# ```
# python3 voice_control/tools/deepspeech/wavTranscriber/main.py
# ```


nlp = spacy.load("en_core_web_sm")
model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])


# takes wav
def transcribe(wav):

    w = wave.open(wav, 'r')

    rate = w.getframerate()

    frames = w.getnframes()

    buffer = w.readframes(frames)

    data16 = np.frombuffer(buffer, dtype=np.int16)

    text = model.stt(data16)

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
def print_result(result):
    prompt = "{t:50s} | {k:10s} | {b:10s}".format(t=result[0], k=result[1], b=str(result[2]))
    print(prompt)


def runner():
    keyword = "forward"

    transcriptions = [transcribe(dat) for dat in conf['audio_wave_path']]
    results = [process(transcription, keyword) for transcription in transcriptions]

    print("")
    print("{t:50s} | {k:10s} | {b:15s}".format(t="input", k="keyword", b="result"))
    print("-"*75)

    [print_result(result) for result in results]
    print("")

def main():
    runner()


if __name__ == "__main__":
    main()





