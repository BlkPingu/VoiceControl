from config import conf

class TranscriberInterface:

    def __init__(self):
        model = deepspeech.Model(conf['model_file_path'], conf['beam_width'])
        model.enableDecoderWithLM(conf['lm_file_path'], conf['trie_file_path'], conf['lm_alpha'], conf['lm_beta'])