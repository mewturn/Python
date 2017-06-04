########################################################
# Plots points, lines and labels using matplotlib.pyplot
########################################################

import matplotlib.pyplot as plt
import numpy as np
import math

# Set graph axes
plt.axis([-5, 5, -5, 5])

x1_list = [0, 1, 0, 1]
x2_list = [0, 1, 1, 0]
y_list = [1, 1, -1, -1]

# Line Plotting
# x = np.arange(-5.0, 5.0, 0.01)
# y = x + 2.5
# plt.plot(x,y,'green')
# plt.annotate('Boundary equation: x2 = x1 + 2.5', xy= (-3, -2), xytext=(-3, -2))

# Point labelling
# plt.annotate('(0,0)', xy = (0, 0), xytext = (0, 0.3))
# plt.annotate('(1,3)', xy = (1, 3), xytext = (1, 3.3))
# plt.annotate('(0,3)', xy = (0, 3), xytext = (0, 3.3))

for i in range(len(x1_list)):
	if y_list[i] == 1:
		colour = "ro"
	else:
		colour = "bo"
	plt.plot(x1_list[i], x2_list[i], colour)

plt.show()

### Resources

# Colours
# https://matplotlib.org/api/colors_api.html

# Markers
# https://matplotlib.org/api/markers_api.html
