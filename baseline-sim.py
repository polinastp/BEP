import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import random
import scipy

from utils import rename_columns, add_time_columns

# Setting a seed 
random.set(123)

# Loading the Data 
data_raw = pd.read_csv('data/data-2010-2024.csv', delimiter=",", skiprows=3)
data_test = pd.read_csv('data/om-2025-test.csv', delimiter=",", skiprows=3 )

data_test['time'] = pd.to_datetime(data_test['time'], format='%Y-%m-%dT%H:%M', errors='coerce')

print(data_raw)




# # 
# 
# # all_data = add_time_columns(data_raw)
# all_data = rename_columns(data_raw)
# # test_data = add_time_columns(data_test)
# test_data = rename_columns(data_test)

# # Aveage the data

# daily_mean_df = all_data.groupby(['year', 'month', 'day']).mean().reset_index()
# daily_mean_test_df = test_data.select_dtypes(include=[np.number]).groupby(['year', 'month', 'day']).mean().reset_index()

