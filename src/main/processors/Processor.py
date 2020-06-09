class LimitedProcess(interfaces.ProcessorInterface):

    def __init__(self, spacy_model):
            model = spacy.load(spacy_model)