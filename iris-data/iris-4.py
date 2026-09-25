"""Recupérer et afficher les données d'iris avec scatter et acatterplot en 3d avec une fonciton a deux variable """

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris 
import numpy as np

iris = load_iris()

x = iris.data
y = iris.target 

f = lambda x,y : np.sin(x) * np.cos(x + y)

X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
    
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)

figure = plt.figure()

ax = figure.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, cmap = 'viridis')

plt.show()


