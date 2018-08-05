import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

def chart(x, y, label, imgfile, textloc):
#    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        plt.annotate(label,
                     xy=(x, y),
                     arrowprops=dict(arrowstyle='->'),
                     xytext=textloc)
        x = [0.01, x]
        y = [y, y]
        ax.fill_between(x, 0.01, y, color = 'lightblue', alpha = .8)

        # ax.legend()
        ax.grid(True)
        plt.ylim((0, 1))
        plt.xlim((0, 1))
        plt.xticks([])
        plt.yticks([])

        plt.xlabel('What you did')
        plt.ylabel('How well you talk about it')

        plt.savefig(imgfile)

chart(.1, .9, 'Great presentation for minimal work',
      'img-generated/pres_gt_work.png', (.25, .5))
chart(.9, .1, 'Amazing work, no presentation',
      'img-generated/work_gt_pres.png', (.2, .3))
chart(.6, .6, 'Okay work and presentation',
      'img-generated/work_pres_balance.png', (.1, 1.0))
