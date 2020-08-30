from interfaces.TranscriberInterface import TranscriberInterface
import deepspeech
import numpy as np
from config import conf
import wave
from utility.Paths import path_to_base

class Transcriber(TranscriberInterface):

    mfp = path_to_base(conf['model_file_path'])
    lmfp = path_to_base(conf['lm_file_path'])
    tfp = path_to_base(conf['trie_file_path'])


    def __init__(self):
        self.model = deepspeech.Model(mfp, conf['beam_width'])
        self.model.enableDecoderWithLM(lmfp, tfp, conf['lm_alpha'], conf['lm_beta'])


    def transcribe_from(data, *args, **kwargs) -> str:
        """transcribe data to string"""
        pass