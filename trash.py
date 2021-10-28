from graphs import *
import pandas as pd

data = pd.read_csv("/home/jaskirats/Code/Python_Plotter_prev/Files/RELIANCE.csv")

pair_plot(data, None, "kde", diagkind=None, marker="#", height=10)