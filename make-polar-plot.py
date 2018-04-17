#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# read csv file
data = pd.read_csv('data.csv')

rows = 2
cols = 1
fignum = 1
fig = plt.figure(figsize=(20,20))

for column in data.columns:
    # polar graph
    ax = plt.subplot(rows, cols, fignum, projection='polar')
    # no angles are above 25 so limit the angle
    ax.set_thetamin(0)
    ax.set_thetamax(25)
    # set a fixed radius to be able to compare easily
    ax.set_rlim((0, 50))
    # get the frequencies
    freq = data[column].dropna().value_counts().sort_index()
    # indexes must be in radians
    indexes = [math.radians(a) for a in freq.index]
    # plot it
    bars = ax.bar(indexes, freq.values, bottom=0.0, width=0.1)
    # add title
    plt.title(column)
    # increment figure number
    fignum += 1

plt.tight_layout(pad=3)

plt.savefig('polar-plots.png')
plt.close()
