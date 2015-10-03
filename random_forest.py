__author__ = 'Amit'
import pandas as pd
import numpy as np
import collections
import sqlite3

activity_labels = pd.read_csv("Data/activity_labels.txt")
print(activity_labels)
features = pd.read_csv("Data/features.txt")
