#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as nm  # importing numpy which is a general purpose array processing package
import pandas as pd  # importing pandas library into python, where pandas is used to analyze data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


# In[4]:


X = nm.array([[1, 0], [2, 0], [3, 0], [6, 0], [6, 0], [7, 0], [10, 0], [11, 0]])
print "Dataset with total 8 points: \n ", X, "\n Size: ", len(X)
y = nm.array([0, 0, 1, 1, 1, 0, 0, 0])
print "\n Class label for dataset X Y:", y
# train_test_split splits arrays or matrices into random subsets for train and test data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=None, shuffle=False, stratify=None)
print "\n X Training Data :\n", x_train
print "\n Y Training Data :", y_train


# In[6]:


# To normalize the features of data, individually thus standardize the data
standard_scalar = StandardScaler()
# X-test data is fitted and transformed
x_train = standard_scalar.fit_transform(x_train)
x_test = standard_scalar.transform(x_test)
print "X_train: ", x_train, "\n X_test: ", x_test


# In[8]:


# Initializing KNN Classifier with 3 and fitting the data to classifier thus predicting the Labels for x-test data
KNNclassifier = KNeighborsClassifier(n_neighbors=3)  # Created KNN Classifier object
# Train the model using the training sets
KNNclassifier.fit(x_train, y_train)
# Predict y output i.e. Labels for X-test data
y_predicted_output = KNNclassifier.predict(x_test)
print "\nPredicted class labels for testing data Y: ", y_predicted_output


# In[9]:


# Compute confusion matrix to evaluate the accuracy, sensitivity, specificity of a classification.
confusion_matrix_result = confusion_matrix(y_test, y_predicted_output)
print "\nConfusion Matrix\n", confusion_matrix_result


# In[10]:


#Accuracy = (TP+TN)/ (TP+FN+TN+FP)
total_sum = confusion_matrix_result[0,0]+confusion_matrix_result[0,1]+confusion_matrix_result[1,0]+confusion_matrix_result[1,1]
accuracy = (confusion_matrix_result[0,0]+confusion_matrix_result[1,1])/total_sum
print "\nAccuracy : ", accuracy


# In[11]:


#Sensitivity = TP/(TP+FN)
sensitivity = confusion_matrix_result[1,1]/(confusion_matrix_result[1,0]+confusion_matrix_result[1,1])
print 'Sensitivity : ', sensitivity


# In[12]:


#Specificity = TN/(TN+FP)
specificity = confusion_matrix_result[0,0]/(confusion_matrix_result[0,0]+confusion_matrix_result[0,1])
print 'Specifity : ', specificity


# In[ ]:




