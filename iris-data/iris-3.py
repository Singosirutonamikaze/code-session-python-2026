"""Recupérer et afficher les données d'iris avec scatter et acatterplot en 3d"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris 
import numpy as np

iris = load_iris()

x = iris.data
y = iris.target 

sns.scatterplot(x = x[:, 2],  hue = y, palette='deep')
plt.show()

