import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import pandas as pd
from math import pi

def awards(think, connect, innovate, design, motivate, control,
           label, imgfile):
#    with plt.xkcd():
        fig, ax = plt.subplots()



        df = pd.DataFrame({
            'group': [label],
            'think': [think],
            'connect': [connect],
            'innovate': [innovate],
            'design': [design],
            'movivate': [motivate],
            'control': [control]
        })

        categories=list(df)[1:]
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values=df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        values

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

        # Draw ylabels
        # ax.set_rlabel_position(0)
        plt.yticks([10,20,30], ["10","20","30"], color="grey", size=0)
        plt.ylim(0, 1)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)
        # plt.show()

        plt.savefig(imgfile)

awards(.4, .95, .1, .4, .0, .6,
       'Single-dimensional team', 'img-generated/awards_4628.png')
awards(.8, .2, .2, .8, .6, .7,
       'Inspire candidate team', 'img-generated/awards_inspire.png')
awards(.95, .95, .8, .8, .75, .9,
       'Strong inspire candidate', 'img-generated/awards_strong_inspire.png')
awards(.95, .95, 1.2, .95, 1.6, .8,
       'Supers Inspire Winner', 'img-generated/awards_8496.png')
