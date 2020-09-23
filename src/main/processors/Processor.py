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


    def metadata_to_string(self, metadata):
        """join all words of a transcription to a sentence"""
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


    def process_keyword_csv(self, transcription, keyword):
            """Process the transcripted string and look for a keyword"""

            doc = self.nlp(transcription)

            texts = [token.text for token in doc]

            if keyword in texts:
                return 1
            else:
                return 0


    def to_df(self, data, cols):
        """build dataframe from processed"""
        df = pd.DataFrame.from_records(data, columns = cols)
        return df


    def run(self, data, *args, **kwargs):
        """run the processor"""

        if kwargs.get('csv', False):
            data['TRANSCRIPTION_STRING'] = data['TRANSCRIPTION'].apply(lambda trans: self.metadata_to_string(trans))

            data['TRANS_CONFIDENCE'] = data['TRANSCRIPTION'].apply(lambda trans: trans.confidence)

            data['RESULT'] = data.apply(lambda x: self.process_keyword_csv(x['TRANSCRIPTION_STRING'],x['EXPECTED_TEXT']),axis=1)

            print(data)
            data.to_csv('dump.csv')

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







