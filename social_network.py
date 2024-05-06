#%%
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

folder = Path(__file__).parent
file = Path(folder, "data", "social_network_data.csv")

df = pd.read_csv(file)
df_filtered = df[df["friends"] < 100]
#%%

counts = df["friends"].value_counts()
print(counts)
plt.bar(counts.index, counts)
plt.show()

#%%

print(df.sort_values(by=["friends"], ascending=False))
print(max(df['friends']))

# %%
print(df.mean())
print(df_filtered.mean())
# %%

print(df.median())
print(df_filtered.median())

# %%
print(df.quantile(0.75))
# %%
print(df.var())
print(df_filtered.var())
# %%
print(df.std())
print(df_filtered.std())
# %%
print(df.describe())
# %%

print(df.head(3))
print(df.tail(5))
# %%
print(df.cov())
print(df_filtered.cov())
# %%
print(df.corr())
print(df_filtered.corr())
# %%

plt.scatter(df_filtered["friends"], df_filtered["minutes"])
coeff = np.polyfit(df_filtered["friends"], df_filtered["minutes"], 1)
p = np.poly1d(coeff)
x = np.linspace(0, 50, 100)
plt.plot(x, p(x), "r-")
plt.show()


# %%
