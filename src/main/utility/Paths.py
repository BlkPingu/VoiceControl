import os
from config import conf
import pandas as pd

def path_to_base(path):
    return os.path.join(conf['base_path'], path)

def from_csv(csv_path, uuid_col_name, wav_path_col_name):
    return [{'UUID':row[uuid_col_name], 'PATH':row[wav_path_col_name]} for i, row in pd.read_csv(csv_path).iterrows()]