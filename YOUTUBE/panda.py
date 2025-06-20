import pandas as pd
import numpy as np
pf = pd.read_csv('/Users/swagatsouravdhar/SEMISTER2/PYTHON/YOUTUBE/customer_anazylses-data.csv')
pf.columns.str.strip()
pf.head()
print(pf)
print("Zip Code : ")
print(pf["Zip Code"])