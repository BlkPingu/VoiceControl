from interfaces.TranscriberInterface import TranscriberInterface
import deepspeech
import numpy as np
from config import conf
import wave
from utility.Paths import path_to_base
import time

class Transcriber(TranscriberInterface):




    def __init__(self):

        mfp = path_to_base(conf['model_file_path'])
        lmfp = path_to_base(conf['lm_file_path'])
        tfp = path_to_base(conf['trie_file_path'])

        self.model = deepspeech.Model(mfp, conf['beam_width'])
        self.model.enableDecoderWithLM(lmfp, tfp, conf['lm_alpha'], conf['lm_beta'])
        self.progress = 0
        self.lambda_count = 1
        self.df_size = 0


    def get_df_size(self):
        """get results_df"""
        return self.df_size

    def set_df_size(self, new):
        """set results_df"""
        self.df_size = new

    def get_progress(self):
        """get results_df"""
        return self.progress

    def set_progress(self, new):
        """set results_df"""
        self.progress = new

    def get_lambda_count(self):
        return self.lambda_count

    # Print iterations progress
    def printProgressBar(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()


    def update_progress_bar(self):
        time.sleep(0.1)
        new_progress = self.get_progress() + 1
        self.set_progress(new_progress)
        self.printProgressBar(self.get_progress(), self.get_lambda_count() * self.get_df_size(), prefix = 'Progress:', suffix = 'Complete', length = 50)

    def transcribe_from(data, *args, **kwargs) -> str:
        """transcribe data to string"""
        pass