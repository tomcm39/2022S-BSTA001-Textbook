#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    
    plt.style.use("fivethirtyeight")
    fig,ax = plt.subplots()
    ax.bar([-1,0,1],[0.2,0.5,0.3])

    ax.set_xticks([-1,0,1])
    ax.set_yticks([0,0.2,0.3,0.5])
    
    ax.set_xlabel(r"Support of $Y$",fontsize=10)
    ax.set_ylabel("Probability",fontsize=10)

    fig.set_tight_layout(True)
    fig.set_size_inches(6,3)

    plt.savefig("pmfviz.pdf")
    
