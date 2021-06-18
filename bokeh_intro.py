    
from bokeh.models import HoverTool, ColumnDataSource

plot_values = [1,2,3,4,5]
plot_colors = ['#0173b2', '#de8f05']

from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)

xs, ys = zip(*grid)
print(xs)
print(ys)

colors = [plot_colors[i%2] for i in range(len(grid))]
print(colors)

alphas = np.linspace(0, 1, len(grid))

source = ColumnDataSource(
    data = {
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)


from bokeh.plotting import figure, output_file, show

output_file("Basic_Example.html", title="Basic Example")
fig = figure(tools="hover")
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Value": "@x, @y",
    }
show(fig)