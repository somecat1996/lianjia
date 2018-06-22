import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D
import csv

DataIn = csv.reader(open('coordinate.csv', 'r'))
x, y, z = [], [], []
for row in DataIn:
    x.append(eval(row[1]))
    y.append(eval(row[2]))
    z.append(eval(row[3]))
print(min(x), max(x))
print(min(y), max(y))
print(min(z), max(z))
x = np.array(x)
y = np.array(y)
z = np.array(z)
#####################################################
n = 1024
X = np.linspace(120.5, 122, n)
Y = np.linspace(30.5, 32, n)
X, Y = np.meshgrid(X, Y)
plt.contour(x, y, z)
#####################################################
# gammas = [0.8, 0.5, 0.3]
# fig, axes = plt.subplots(nrows=2, ncols=2)
# axes[0, 0].set_title('Linear normalization')
# axes[0, 0].hist2d(x, y, bins=100)
# for ax, gamma in zip(axes.flat[1:], gammas):
#     ax.set_title('Power law $(\gamma=%1.1f)$' % gamma)
#     ax.hist2d(x, y,
#               bins=100, norm=mcolors.PowerNorm(gamma))
# fig.tight_layout()
# plt.show()
#####################################################
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(x, y, z, )
# plt.show()
#####################################################
# ax = plt.subplot(111, projection='3d')
# ax.scatter(x, y, z, cmap='rainbow', alpha=0.4)
#
# ax.set_zlabel('Z')
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()
#####################################################
