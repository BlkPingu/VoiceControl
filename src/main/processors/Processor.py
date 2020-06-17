from interfaces.ProcessorInterface import ProcessorInterface
import pandas as pd
import spacy

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


    def process(self, str:transcription, str:keyword):
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


    def append_rows(data):
        """append new rows to existing results_df"""
        pass


    def print_results(self):
        print(self.results_df)