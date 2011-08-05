# -*- coding: utf-8 -*-
from svm import *
from svmutil import *

prob = svm_problem([1,-1], [[1, 1.8, 0.9, 5, 3], [0, -0.7, -3, 1, -2]])
param = svm_parameter('-t 1 -c 3')
m = svm_train(prob, param)

p_labels, p_acc, p_vals = svm_predict([1,1], [[1, 1, 1, 3, 5],[1, 2, 1, 5, 2]], m)
print p_labels
