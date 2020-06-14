import deepspeech
import numpy as np
import speech_recognition as sr
from config import conf
import spacy


sample_rate=16000

nlp = spacy.load("en_core_web_sm")
model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])

r = sr.Recognizer()
with sr.Microphone(sample_rate=sample_rate) as source:
    print("Say Something")
    audio = r.listen(source)

    fs = audio.sample_rate
    audio = np.frombuffer(audio.frame_data, np.int16)
    print(model.stt(audio))


