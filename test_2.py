import numpy as np
import pandas as pd
x = np.arange("2019-09-01T00:00", "2020-03-01T00:00", step=np.timedelta64(10, 'm'), dtype='datetime64[m]')
y = np.random.randint(100, 500, size=26208)

df = pd.DataFrame({'value': y}, index=x)
df.to_csv(path_or_buf="input/timeseries_q7.csv")
