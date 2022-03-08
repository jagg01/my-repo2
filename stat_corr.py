import numpy as np
import pandas as pd


def corr_matrix(dataframe, xval_col_name):
    """Creates a correlation matrix of the given data frame and orders it by the
    degree of correlation.

    Args:
    dataframe (pandas dataframe): Give the data frame
    xval_col_name (string): Name of the column containing the x-values. This
    column is deleted.

    Returns:
    dataframe_corr (pandas series): List of correlations sorted by the degree of correlatin
    starting with the highest."""
    # get rid of time column, lower triangular and diagonal entries of the correlation matrix
    dataframe = dataframe.drop(columns=[xval_col_name])
    dataframe_corr = dataframe.corr()
    dataframe_corr_np = np.triu(dataframe_corr,k=1)
    dataframe_corr = pd.DataFrame(data = dataframe_corr_np)
    # sort the remaing values according to their absolute value, but keep the sign
    abs_val = dataframe_corr.abs().unstack() #creates series of absolute values
    abs_val = abs_val.reset_index(drop=True) #sets default index
    abs_val = abs_val.sort_values(ascending = False) #sorts by absolute values
    index_val = abs_val.index.values  #array of indexes after sorting by absolute value
    dataframe_corr = dataframe_corr.unstack() #creates series of correlation matrix
    dataframe_corr = dataframe_corr.iloc[index_val] #sort values by index of abs_val
    dataframe_corr = dataframe_corr.reset_index(drop=True) #new default index
    numb_val = dataframe_corr.to_numpy().nonzero() #position of nonzero entries
    dataframe_corr = dataframe_corr.iloc[numb_val]  #only values belonging to the position of nonzero values
    return dataframe_corr
