import numpy as np
import pandas as pd

dates = pd.date_range("2024-04-29", periods=6, freq="D")
s = pd.Series([10, 30, np.nan, 40, 62, 18], index=dates)
print([str(date) for date in dates.tolist()])

rnd = np.random.randn(6, 4)
print(rnd)
df = pd.DataFrame(rnd, index=dates, columns=["A", "B", "C", "D"])
print(df)

print(df[df["A"] > 0])


data = {
    "User": ["user1", "user2", "user4"],
    "Score": [15, 75, 0]
}

scores = pd.DataFrame(data)
print(scores)
