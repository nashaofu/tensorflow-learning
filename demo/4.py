import numpy as np

import pandas as pd

data = pd.read_csv('./demo/iris.data', names=['e_cd', 'e_kb', 'b_cd', 'b_kb', 'cat'])

data.cat.unique()
