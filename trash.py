from graphs import *
import pandas as pd

data = pd.read_csv("/home/jaskirats/Code/Python_Plotter_prev/Files/RELIANCE.csv")

pair_plot(data, kind='auto', marker="s", height=10, diagkind='auto')