# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:34:30 2017

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
train_index = train.index

#------------------------------------------------------------

fig, ax = plt.subplots(nrows = 2,ncols = 2)
fa = train['fault_severity'].value_counts().plot(kind = 'bar',ax=ax[0,0],title="Fault Severity", y = "Frequency")
resourceType = resource_type.loc[resource_type.index.isin(train.index)]
severityType = severity_type.loc[severity_type.index.isin(train.index)]
eventType = event_type.loc[event_type.index.isin(train.index)]
re = resourceType.resource_type.map(lambda x:x.split(' ')[1]).value_counts().plot(kind='bar',ax = ax[0,1],
                                                              title = "Resource Type", y = "Frequency")
fa.set_xlabel("Fault Severity Type"); fa.set_ylabel("Frequency")
re.set_xlabel("Resource Type"); re.set_ylabel("Frequency")

se = severityType.severity_type.value_counts().plot(kind = 'bar',ax = ax[1,0],title = "Severity Type",figsize = [17,10])
se.set_xlabel("Severity Type"); se.set_ylabel("Frequency")

ev = eventType.event_type.map(lambda x:x.split(' ')[1]).value_counts().plot(kind = 'bar',ax = ax[1,1],title = 'Event Type')
ev.set_xlabel("Event Type");ev.set_ylabel("Frequency")

#------------------------------------------------------------

fig,ax = plt.subplots(nrows = 1, ncols = 2)
log_feature.volume.loc[log_feature.index.isin(train.index)].plot(kind = 'box',figsize = [12.0,5.0],title="Volume",ax = ax[0])
log_feature.volume.loc[log_feature.index.isin(train.index)].plot(kind = 'density',figsize = [12.0,5.0],title="Volume",ax = ax[1])
#log_feature_train = log_feature.loc[log_feature.id.isin(train.id)].query('volume<500')

#------------------------------------------------------------

matplotlib.rcParams['figure.figsize'] = (12.0, 7.0)
log_feature_train = log_feature.loc[log_feature.index.isin(train.index)]
log_feature_train.volume = (((np.log2(((log_feature_train.volume - np.mean(log_feature_train.volume))/np.std(log_feature_train.volume))**2))))
fig,ax = plt.subplots(nrows = 1,ncols= 3)
sct.probplot(log_feature_train.volume,dist="norm", plot=plt)
log_feature_train.volume.plot(kind='density', ax = ax[0])
log_feature_train.volume.plot(kind='box', ax = ax[1])
plt.show()





