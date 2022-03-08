import pandas as pd
import numpy as np


def rd_file(filedir,filename):
    """Add an explanation here, variables and what it does
    """
    path_f = filedir + filename
    ptemp1 = pd.read_csv(path_f, r'\s+', header=None,skiprows=1)
    fl = ptemp1[0].values
    no_fl = len(fl)

    cl = open(path_f, "r").readlines()
    line = cl[1].split()
    no_cl = len(line)

    fl_exp = np.zeros((no_cl,no_fl))
    for i in range(no_cl):
        ptemp2 = pd.read_csv(path_f, r'\s+', header=None,skiprows=1)
        fl_exp[i] = ptemp2[i].values
    return fl_exp


def ths_def(fl_exp,threshold):
    useless = (fl_exp < threshold).all(axis=1)
    for i in range(len(useless)):
        if useless[i] is True:
            del_fl_exp = np.delete(fl_exp,i,0)

    return del_fl_exp
