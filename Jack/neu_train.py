from sklearn.datasets import load_iris
import numpy as np
data = np.loadtxt('data/neuro_feat.tsv', delimiter='\t')




from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data[:-1,:], iris.target[:-1]