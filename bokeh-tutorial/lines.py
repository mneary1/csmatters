from bokeh.plotting import figure, HBox, output_file, show, VBox
from bokeh.models import Range1d

# create some data using python lists
x1 = [0, 1, 2, 3, 4, 5,  6,  7, 8,   9, 10]
y1 = [0, 8, 2, 4, 6, 9, 15, 18, 19, 25, 28]

# EXERCISE: create two more data sets, x2, y2 and x3, y3, however
# you want. Make sure the corresponding x and y data are the same length
x2 = [0, 1, 2, 3,  4, 5, 6,  7,  8,  9, 10]
y2 = [1, 3, 5, 8, 13, 7, 2, 12, 15, 16,  4]

x3 = [0, 1, 2, 3, 4, 5,  6,  7, 8,   9, 10]
y3 = [0, 7, 1, 2, 3, 4, 5, 6, 7, 8, 28]

# specify and output static HTML file
output_file("scatter.html")

# EXERCISE: Plot all the sets of points on different plots p1, p2, p3.
# Try setting `color` (or `line_color`) and `alpha` (or `line_alpha`).
# You can also set `line_dash` and `line_width`. One example is given.
p1 = figure(plot_width=300, plot_height=300)
p1.line(x1, y1, size=12, color="red", alpha=0.5)

p2 = figure(plot_width=300, plot_height=300)
p2.line(x2, y2, size=10, color="blue", alpha=0.5, line_dash="dashed")

p3 = figure(plot_width=300, plot_height=300)
p3.line(x3, y3, size=13, color="green", alpha=0.5)

# create a figure
p4 = figure()
p4.line(x1, y1, size=12, color="red", alpha=0.5)
p4.line(x2, y2, size=10, color="blue", alpha=0.5, line_dash="dashed")
p4.line(x3, y3, size=13, color="green", alpha=0.5)

# EXERCISE: add all the same renderers above, on this one plot

# show the plots arrayed in a VBox
show(VBox(HBox(p1, p2, p3),p4))