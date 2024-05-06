#%%
import matplotlib.pyplot as plt
import numpy as np

#%%
plt.plot([-10, -1, 3, 7], [1, 3, 2, 4], "ro-")
plt.ylabel("Some numbers")
plt.show()

#%%
x = np.arange(-10, 10, 0.1)
plt.plot(x, x**2)
plt.show()

# %%
