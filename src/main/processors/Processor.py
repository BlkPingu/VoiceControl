class Processor(interfaces.ProcessorInterface):

    def __init__(self, spacy_model):
            model = spacy.load(spacy_model)


    def process(self, transcriped):
        """Process the transcripted string and look for a keyword"""
            doc = nlp(transcription)

        texts = [token.text for token in doc]

        if keyword in texts:
            return (transcription, keyword, True)
        else:
            return (transcription, keyword, False)


    def to_array(self, data, cols):
        """build dataframe from processed"""
        df = pd.DataFrame.from_records(data, columns = cols)

        return df