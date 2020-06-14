from interfaces.ProcessorInterface import ProcessorInterface
import pandas as pd
import spacy

class Processor(ProcessorInterface):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")


    def process(self, transcription, keyword):
        """Process the transcripted string and look for a keyword"""

        doc = self.nlp(transcription)

        texts = [token.text for token in doc]

        if keyword in texts:
            return (transcription, keyword, True)
        else:
            return (transcription, keyword, False)


    def to_array(self, data, cols):
        """build dataframe from processed"""
        df = pd.DataFrame.from_records(data, columns = cols)

        return df