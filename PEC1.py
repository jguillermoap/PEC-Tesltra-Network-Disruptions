# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 17:43:20 2018

@author: jguillermo_aparicio
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import scipy.stats as sct
import pylab

matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)

train = pd.read_csv('train.csv',index_col=0)
test = pd.read_csv('test.csv',index_col=0)
event_type = pd.read_csv('event_type.csv',index_col=0)
log_feature = pd.read_csv('log_feature.csv',index_col=0)
resource_type = pd.read_csv('resource_type.csv',index_col=0)
severity_type = pd.read_csv('severity_type.csv',index_col=0)