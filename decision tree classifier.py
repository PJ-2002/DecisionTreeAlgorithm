import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type']

data = pd.read_csv("iris.csv", skiprows=1, header=None, names=col_names)

print(data['type'].unique())

label_encoder = LabelEncoder()

data['type'] = label_encoder.fit_transform(data['type'])

print(data.head())

# NODE CLASS

class Node:
    def __init__(self, feature_index = None, threshold = None, info_gain = None, left = None, right = None, value = None) :
        
        self.feature_index = feature_index
        self.left = left
        self.right = right
        self.info_gain = info_gain
        self.value = value
        self.threshold = threshold
