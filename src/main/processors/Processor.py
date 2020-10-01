from interfaces.ProcessorInterface import ProcessorInterface
import pandas as pd
import spacy
from config import conf
from pandas.core.common import flatten
from itertools import product
import time




class Processor(ProcessorInterface):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.results_df = pd.DataFrame()
        self.progress = 0
        self.lambda_count = 2
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

    def get_results_df(self):
        """get results_df"""
        return self.results_df

    def set_results_df(self, new):
        """set results_df"""
        self.results_df = new

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


    def finish_run(self, data):
        data.to_csv(conf['result_csv'])
        print('result saved as: ' + conf['result_csv'])

    def metadata_to_string(self, metadata):
        """join all words of a transcription to a sentence"""
        self.update_progress_bar()
        words = [item.character for item in metadata.items]
        return ''.join(words)


    def process_keyword(self, keyword, confidence, transcription):
        """Process the transcripted string and look for a keyword"""

        doc = self.nlp(transcription)

        texts = [token.text for token in doc]

        if keyword in texts:
            return (transcription, keyword, confidence, True)
        else:
            return (transcription, keyword, confidence, False)

    def to_df(self, data, cols):
        """build dataframe from processed"""
        df = pd.DataFrame.from_records(data, columns = cols)
        return df

    def get_confidence(self, trans):
        self.update_progress_bar()
        return trans.confidence

    def run(self, data, *args, **kwargs):
        """run the processor"""

        if kwargs.get('csv', False):

            self.set_df_size(len(data.index))

            data['TRANSCRIPTION_STRING'] = data['TRANSCRIPTION'].apply(lambda trans: self.metadata_to_string(trans))

            data['TRANS_CONFIDENCE'] = data['TRANSCRIPTION'].apply(lambda trans: self.get_confidence(trans))

            self.finish_run(data)

        else:
            results = list()
            keywords = conf['keywords']

            for keyword, metadata in product(keywords, data):

                transcription = self.metadata_to_string(metadata)

                confidence = metadata.confidence

                result = self.process_keyword(keyword, confidence, transcription)
                results.append(result)


            df = self.to_df(results, ['input', 'keyword', 'conficence', 'result'])

            self.set_results_df(df)







