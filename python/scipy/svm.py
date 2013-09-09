#-*- coding:utf-8 -*-
 
from svm import *
from svmutil import *
 
# For learning
t_label = [1,-1,1,-1]
t_data = [
    [1.0, 2.0, 3.0],
    [3.0, 1.5, 1.0],
    [2.0, 3.0, 4.0],
    [0.5, 1.0, 1.5]
    ]
problem = svm_problem(t_label, t_data)
parameter = svm_parameter('-s 0 -t 0')
t = svm_train(problem, parameter)
 
# For predict
p_label = [1, 1, -1, -1]
p_data = [
    [0.3, 0.9, 1.2],
    [2.0, 3.0, 4.5],
    [3.0, 1.0, 0.3],
    [1.0, 0.5, 0.25]
    ]
result = svm_predict(p_label, p_data , t)
 
print "[Result]"
for r in result:
    print r
