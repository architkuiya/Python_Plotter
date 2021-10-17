import matplotlib.pyplot as plt
import seaborn as sb
import pandas 


def bar_plot(x, y):
    plt.bar(x,y)
    # plt.xlabel(x)
    # plt.ylabel(y)
    plt.show()

def scatter_plot(x, y):
    plt.scatter(x,y)
    # plt.xlabel(x)
    # plt.ylabel(y)
    plt.show()

def hist_plot(x, y):
    plt.hist(x)
    plt.hist(y)
    # plt.xlabel(x)
    # plt.ylabel(y)
    plt.show()

def plot(x, y):
    plt.plot(x,y)
    # plt.xlabel(x)
    # plt.ylabel(y)
    plt.show()

def pair_plot(dataframe):
    sb.pairplot(dataframe)
    plt.show()