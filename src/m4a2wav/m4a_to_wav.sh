#!/bin/bash

pip3 install pydub

# Rename folder M4a_files as wav_files
# mv M4a_files wav_files

brew install ffmpeg

brew update && brew upgrade ffmpeg

tar -xvzf M4a_files.tar.gz

find M4a_files/ -name 'tapping_results.*' -delete

python3 rename.py

python3 convert.py

mv M4a_files wav_files