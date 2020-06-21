conf = {
    'keywords': ['left', 'right', 'forward', 'backward'],
    'model_file_path': 'models/deepspeech-0.6.1-models/output_graph.pbmm',
    'trie_file_path': 'models/deepspeech-0.6.1-models/trie',
    'lm_file_path':'models/deepspeech-0.6.1-models/lm.binary',
    'audio_wave_path': [
        'audio_recordings/exports/fox.wav',
        'audio_recordings/exports/left.wav',
        'audio_recordings/exports/right.wav',
        'audio_recordings/exports/forward.wav',
        'audio_recordings/exports/backward.wav'
        ],
    'lm_alpha': 0.75,
    'lm_beta': 1.85,
    'beam_width': 500
}