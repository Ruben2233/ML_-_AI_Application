"""
Created on Thu Oct 18 10:38:11 2018

@author: Ruben Buendia
"""

#Enter the directory where the data was downloaded
import os
os.chdir("/home/kkfm110/ML_AI_Exercise")


#Load Libreries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.datasets import load_svmlight_file
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error
from bland_altman import bland_altman_plot



pt_X,pt_y  = load_svmlight_file('dataset.csr')

svr_lin = SVR(kernel='linear', C=1)
lasso = linear_model.Lasso()
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.0005)

y_pred = cross_val_predict(svr_rbf, pt_X, pt_y, cv=20)

Fig1, ax = plt.subplots()
ax.scatter(pt_y, y_pred, edgecolors=(0, 0, 0))
ax.plot([pt_y.min(), pt_y.max()], [pt_y.min(), pt_y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
Fig1.savefig('Regression_plot.svg',  format='svg', dpi=1200)



Fig2, ax = plt.subplots(1, figsize =(10,6))
my_bland_altman_plot = bland_altman_plot(pt_y, y_pred, ax = ax)
Fig2.savefig('Bland-Altman_plot.svg',  format='svg', dpi=1200)



a = y_pred-pt_y
Relative_Error = np.mean(abs(y_pred-pt_y))*100/np.mean(pt_y)

print('corr = %s' %np.corrcoef(pt_y,y_pred)[0,1])
print('Mean_Squared_Error = %s' %mean_squared_error(pt_y,y_pred))
print('Relative_Error = %s%%\n' %Relative_Error)


