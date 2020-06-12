from deepspeech import Model
import numpy as np
import speech_recognition as sr
from config import conf


sample_rate=16000

nlp = spacy.load("en_core_web_sm")
model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])

r = sr.Recognizer()
with sr.Microphone(sample_rate=sample_rate) as source:
    print("Say Something")
    audio = r.listen(source)

    rate = audio.getframerate()
    frames = audio.getnframes()
    buffer = audio.readframes(frames)
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


