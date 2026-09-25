import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

figure, ax = plt.subplots(figsize = (6,4))

ax.plot(x, np.sin(x), label="sinus")
ax.plot(x, np.cos(x), label="cosinus")
ax.set_xlabel("x")
ax.set_ylabel("valeur")

plt.show()










