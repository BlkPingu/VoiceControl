import deepspeech
import wave
import numpy as np
import spacy
from config import conf

nlp = spacy.load("en_core_web_sm")
model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])






filename = conf['audio_wave_path'][0]
w = wave.open(filename, 'r')
rate = w.getframerate()
frames = w.getnframes()
buffer = w.readframes(frames)
data16 = np.frombuffer(buffer, dtype=np.int16)
text = model.stt(data16)

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

