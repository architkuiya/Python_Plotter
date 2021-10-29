import matplotlib.pyplot as plt
import seaborn as sb
import pandas 



def bar_plot(x, y, height, width, align, color, linewidth):
    fig = plt.figure()
    plt.bar(x, y, width=width, align=align, color=color, linewidth=linewidth)
    plt.show()


def scatter_plot(x, y, color, mark_size, linewidth, cmap, alpha):
    plt.scatter(x,y, s=mark_size, c=color, linewidth=linewidth, cmap=cmap, alpha=alpha)
    plt.show()

def hist_plot(x, bins, range, density, weights, align, color):
    plt.hist(x, bins=bins, range=range, density=density, weights=weights, align=align, color=color)
    plt.show()

def plot(x, y, color, linewidth):
    plt.plot(x, y, color=color, linewidth=linewidth)
    plt.show()

def pair_plot(dataframe, kind, diagkind, marker, height):
    sb.pairplot(dataframe, kind=kind, diag_kind=diagkind, markers=marker, height=height)
    plt.show()