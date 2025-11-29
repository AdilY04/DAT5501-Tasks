import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('Week_10/data.csv', sep=';')
#print(data.head())
#dataset is clean and has numerical values
data.columns = data.columns.str.replace(r'[\x00-\x1F\x7F]', '', regex=True)

features = data.drop(columns=['Target'])
X = features
y = data['Target']

dtree = DecisionTreeClassifier(max_depth=3, min_samples_split=20, min_samples_leaf=10, max_leaf_nodes=20)
dtree = dtree.fit(X, y)

plt.figure(figsize=(20, 12))
tree.plot_tree(dtree, feature_names=features.columns)
plt.show()