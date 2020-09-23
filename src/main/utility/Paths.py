import os
from config import conf
import pandas as pd

def path_to_base(path):
    return os.path.join(conf['base_path'], path)