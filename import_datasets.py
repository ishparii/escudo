import pandas as pd 
import numpy as np 
import csv as csv 
import glob 
import pickle
from datetime import datetime 
import matplotlib.pyplot as plt 

print("Starting!")

names = ['src', '<->', 'dest', 'in_frames', 'in_bytes', 'out_frames', 'out_bytes', 'total_frames', 'total_bytes', 'rel_start', 'duration']
to_drop = ['<->', 'total_bytes', 'total_frames']

# Import traffic data
ddos_df = pd.read_csv('../ddostrace.pcap.csv', header=None, skiprows=5, names=names)
ddos_df = ddos_df.drop(to_drop, axis=1)

# 1. Organize dataframe so that we have all entries as:
#       src | dest | bytes from src to dest | frames from src to dest

# Iterate through samples, reformatting any samples which contain only inbound
# data such that they now express an 
#       ip_address_B <- ip_address_A 
# relationship as opposed to 
#       ip_address_A -> ip_address_B
for row_index, row in ddos_df.iterrows():
    if row['in_bytes'] != 0:
        ddos_df.loc[row_index, 'src'] = row['dest']
        ddos_df.loc[row_index, 'dest'] = row['src']
        ddos_df.loc[row_index, 'out_frames'] = row['in_frames']
        ddos_df.loc[row_index, 'out_bytes'] = row['in_bytes']

# Then drop all in_bytes, in_frames columns
ddos_df = ddos_df.drop(['in_frames', 'in_bytes'], axis=1)
ddos_df['traffic_rate'] = ddos_df['out_bytes'] / ddos_df['duration']

# Saves the dataframe into a file for later use. The equivalent file-opening
# code is:
# with open('clean_ddos_data.pickle', 'rb') as handle:
#   ddos_clean = pickle.load(handle)

with open('clean_ddos_data.pickle', 'wb') as handle:
    pickle.dump(ddos_df, handle)
