import deepspeech
from config import conf
import wave
import numpy as np

# Run in Bachelorarbeit/Code/DeepSpeech_VirtualEnv:
# ```
# python3 voice_control/tools/deepspeech/wavTranscriber/main.py
# ```

def transcribe(wav):

    model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])

    model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])

    w = wave.open(wav, 'r')

    rate = w.getframerate()

    frames = w.getnframes()

    buffer = w.readframes(frames)
    #print(rate)
    #print(model.sampleRate())

    type(buffer)

    data16 = np.frombuffer(buffer, dtype=np.int16)

    #type(data16)

    text = model.stt(data16)
    return text


def main():
    [print(transcribe(dat)) for dat in conf['audio_wave_path']]


if __name__ == "__main__":
    main()