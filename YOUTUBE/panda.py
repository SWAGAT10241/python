import pandas as pd
import numpy as np
pf = pd.read_csv('/Users/swagatsouravdhar/SEMISTER2/PYTHON/YOUTUBE/customer_anazylses-data.txt', sep='\t')
pf.head()
print(pf)
print(pf["Zip Code"].unique())