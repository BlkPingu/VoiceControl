from interfaces.TranscriberInterface import TranscriberInterface
import deepspeech
import numpy as np
from config import conf
import wave

class Transcriber(TranscriberInterface):

    def __init__(self):
        self.model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
        self.model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])


    def transcribe_from(data) -> str:
        """transcribe data to string"""
        pass