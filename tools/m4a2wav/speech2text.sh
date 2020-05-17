#!/bin/bash

# deepspeech --model models/deepspeech-0.6.1-models/output_graph.pbmm --lm models/deepspeech-0.6.1-models/lm.binary --trie models/deepspeech-0.6.1-models/trie --audio /tools/m4a2wav/wav_files/test.wav

deepspeech --model models/deepspeech-0.6.1-models/output_graph.pbmm --audio /tools/m4a2wav/wav_files/test.wav