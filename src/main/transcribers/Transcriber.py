import interfaces.TranscriberInterface
class Transcriber(interfaces.TranscriberInterface):

    def __init__(self):
        model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
        model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])


    def transcribe_from(data) -> str:
        """transcribe data to string"