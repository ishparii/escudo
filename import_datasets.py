import pandas as pd 
import numpy as np 
import csv as csv 
import glob 
from datetime import datetime 
import matplotlib.pyplot as plt 

print("Starting!")

# Import both ddos and regular traffic
ddos_df = pd.read_csv('../ddostrace.pcap.csv', header=TODO)

ddos_df.columns = ['src', '<->', 'dest', 'in_frames', 'in_bytes', 'out_frames', 'out_bytes', 'total_frames', 'total_bytes', 'rel_start', 'duration']
ddos_df = ddos_df.drop('<->', 1)
ddos_df = ddos_df.drop('total_frames', 'total_bytes', 1)



# The samples-features matrix will be organized such that each sample is a
# communication instance between two IPs, but strictly one in which we
# only talk about the data sent one way. Thus, it will look like:
# 
#   src | dest | frames | bytes | duration | data_rate
# 
# (for passive dataset)
# Question: Are the amount of to_IP and from_IP instances equal?
#           That is, if we observe 20 bytes, A -> B, will we also see
#           20 bytes, B <- A? If this is the case, then we can effectively
#           discard any B <- A's, since we'll find that data transmission in the A -> B.
#           --
#           Probably not. If there are multiple communication instances between
#           two IPs, then we'll just have to aggregate them somehow. 



# Extract additional features
flags = ['syn', 'ack', 'fin', 'push', 'urgent', 'unreachable']

def extract_feature(dt, feature):
    if feature in dt.lower():
        return 1
    else:
        return 0

for flag in flags:
    ddos_df[flag] = np.vectorize(extract_feature)(ddos_df['_ws.col.Info'], flag)
    regular_df[flag] = np.vectorize(extract_feature)(regular_df['_ws.col.Info'], flag)

# Specifying protocol for later calculation
def protocol(dt, index):
    if dt == index:
        return 1
    else:
        return 0

ddos_df.insert(5, 'tcp', np.vectorize(protocol)(ddos_df['ip.proto'], 6))
ddos_df.insert(6, 'icmp', np.vectorize(protocol)(ddos_df['ip.proto'], 1))
regular_df.insert(5, 'tcp', np.vectorize(protocol)(regular_df['ip.proto'], 6))
regular_df.insert(6, 'icmp', np.vectorize(protocol)(regular_df['ip.proto'], 1))

def time(dt):
    date_and_time = dt.split('.')
    return datetime.strptime(date_and_time[0], "%b %d, %Y %H:%M:%S")

ddos_df.insert(2, 'time', ddos_df['frame.time'].map(time))
regular_df.insert(2, 'time', regular_df['frame.time'].map(time))

def add_label(dt, label):
    dt['label'] = label

ddos_df['label'] = 'attack'
regular_df['label'] = 'regular'

print("\nDDOS DATA:\n{0}".format(ddos_df.describe()))
print("\nREGULAR DATA:\n{0}".format(regular_df.describe()))

print("\nDDOS HEAD:\n{0}".format(ddos_df.head()))
print("\nREGULAR DATA:\n{0}".format(regular_df.head()))

print("Finished!")