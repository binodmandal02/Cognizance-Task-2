# Data formatting
# From the given dataset, find the missing values(Nan/NA/-/Nil) and change those values into an appropriate number.

import pandas as pd
import numpy as np

data_frame = pd.read_csv('dataset.csv')
data_frame = data_frame.replace(np.nan, 69)
data_frame.to_csv('final_dataset.csv')