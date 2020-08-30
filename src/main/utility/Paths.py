import os
from config import conf

def path_to_base(path):
    return os.path.join(conf['base_path'], path)