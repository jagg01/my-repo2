import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_save(xval_col_name,dataframe,path):
    """ Creates plots of the columns of a dataframe and saves them.

    Args:
    dataframe: given Data frame.
    xval_col_name (string): Name of the column which contains the x-values.

    Result:
    save: For each column a plot is generated and saved as pdf."""

    plot = sns.pairplot(dataframe,x_vars=xval_col_name,height = 5)
    save = plt.savefig(os.path.join(path,str(dataframe)+'.pdf'))
    return plot, save
