from interfaces.ProcessorInterface import ProcessorInterface
import pandas as pd
import spacy
from config import conf
from pandas.core.common import flatten
from itertools import product



class Processor(ProcessorInterface):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.results_df = pd.DataFrame()


    def get_results_df(self):
        """get results_df"""
        return self.results_df


    def set_results_df(self, new):
        """set results_df"""
        self.results_df = new


    def process_keyword(self, transcription, keyword):
        """Process the transcripted string and look for a keyword"""
        doc = self.nlp(transcription)

        texts = [token.text for token in doc]

        if keyword in texts:
            return (transcription, keyword, True)
        else:
            return (transcription, keyword, False)


    def to_df(self, data, cols):
        """build dataframe from processed"""
        df = pd.DataFrame.from_records(data, columns = cols)
        return df


    def run(self, transcriptions):
        """run the processor"""
        results = list()

        keywords = conf['keywords']

        for keyword, transcription in product(keywords, transcriptions):
              result = self.process_keyword(transcription, keyword)
              results.append(result)


        df = self.to_df(results, ['input', 'keyword', 'result'])

        self.set_results_df(df)