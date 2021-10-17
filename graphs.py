import matplotlib.pyplot as plt
import seaborn as sb
import pandas 


def bar_plot(x, y):
    plt.bar(x,y)
    plt.xlabel(x)
    plt.ylabel(y)

def scatter_plot(x, y):
    plt.scatter(x,y)
    plt.xlabel(x)
    plt.ylabel(y)

def hist_plot(x, y):
    plt.hist(x)
    plt.hist(y)
    plt.xlabel(x)
    plt.ylabel(y)

def plot(x, y):
    plt.plot(x,y)
    plt.xlabel(x)
    plt.ylabel(y)

def pair_plot(dataframe):
    sb.pairplot(dataframe)
    plt.show()