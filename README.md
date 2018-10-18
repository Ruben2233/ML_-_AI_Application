# ML_AI_Application
Lipophilicity Regression Modelling 

In this repository, a regression model targeting values of Lipophilicity(logD7.4) is presented and validated. 

First step was generating signature descriptors as set of attributes. Relation between the target variable, i.e. Lipophilicity(logD7.4), and other available measurements such as molecular weight were tested, however they resulted in poor correlation.

Thereafter available machine learning methods for regression were selected. Linear and ridge regression were discarded because they are suboptimal to handle sparse data. Lasso and support vector regressors were selected. The Lasso method performed very poorly with default parameters; otherwise support vector regressors performance was much higher, thus they were selected. Linear and RBF kernels were tested. Manual tuning of the penalty parameter in the case of linear kernel, and the penalty plus gamma in the case of RBF, was performed. Finally a support vector regressor where the penalty parameter set at 100 and gamma set at 5e-4, was the top performer model.

Regression and Bland-Altman plots are provided for performance evaluation. Bland-Altman plots provide Bias which is a suitable measures of accuracy and Limits of Agreement, i.e 1.96*std of the differences or 95% confidence intervals, which is a suitable measure of precision. In addition, the correlation coefficient, the mean squared error, and the relative error were provided.

Results were: 
Correlation Coefficient = 0.79
MSE = 0.56
Relative Error = 25%
BIAS = 0.0
LOA = 1.47

The model resulted very acurate, however precision was not as great.
