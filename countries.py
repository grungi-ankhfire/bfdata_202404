import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

file_path = Path(__file__).parent

df = pd.read_csv(Path(file_path, "data", "countries.csv"))

print(df)

x = df["Name"]
y = df["Literacy"]

plt.xlabel("Country")
plt.ylabel("Literacy")
plt.plot(x, y)

plt.show()