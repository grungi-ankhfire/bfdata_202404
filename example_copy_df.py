import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4))

df2 = df[df[0] > 0]

df.loc[[True, False, False, False, False, False], 3] = 1000

print(df)