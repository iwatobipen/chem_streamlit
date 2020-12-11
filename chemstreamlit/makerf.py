from sklearn.ensemble import RandomForestClassifier
import numpy as np
import datamaker
import pickle

sdf = './solubility.train.sdf'
rfc = RandomForestClassifier()
x, y = datamaker.make_data(sdf)
rfc.fit(x, y)
pickle.dump(rfc, open('rf.pkl', 'wb'))