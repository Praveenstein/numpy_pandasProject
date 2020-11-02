import numpy as np
import matplotlib.pylab as plt

x_axis = np.arange(-50, 50, 0.5)
y_axis_sin = np.sin(x_axis)
y_axis_cos = np.cos(x_axis)
y_axis_sig = 1 / (1 + np.exp(-x_axis))

fig, axs = plt.subplots(3)
fig.suptitle('Sine, Cosine and Sigmoid Plots')
axs[0].plot(x_axis, y_axis_sin)
axs[1].plot(x_axis, y_axis_cos)
axs[2].plot(x_axis, y_axis_sig)
plt.show()
