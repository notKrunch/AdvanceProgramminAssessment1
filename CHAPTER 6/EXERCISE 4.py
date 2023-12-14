import matplotlib.pyplot as plot

# X, Y axis of Solid line
xsolids = [1, 6]
ysolids = [2, 8]

# X, Y axis of Dotted line
xdots = [1, 2, 6, 8]
ydots = [3, 8, 1, 10]

# Plotting
plot.plot(xsolids, ysolids, label='Solid Line')
plot.plot(xdots, ydots, 'r--',label='Dotted Line') 

# Adding labels and legend
plot.title('Line Diagram')
plot.xlabel('X-axis')
plot.ylabel('Y-axis')
plot.legend()

# Show the plot
plot.show()
