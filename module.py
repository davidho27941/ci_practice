import numpy as np
import pandas as pd 
import scipy 
import itertools

def psudo_data_generator(MODEL):
    if MODEL == 'A':
        arr = np.random.rand(10).astype('f')
        combi = [x for x in itertools.combinations(arr, 2)]
    return np.array(combi)

def psudo_chi2_calculator(MODEL, DATA):
    if MODEL == 'A':
        mean = (DATA[:,0] - DATA[:,1]).sum()/len(DATA)
        chi2 = (DATA[:,0] - mean)/mean + (DATA[:,1] - mean)/mean
    return chi2.sum()
    
