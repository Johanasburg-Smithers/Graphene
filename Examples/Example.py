# To use this module, put the file 'Graphene.py'
# Into the directory
# 'C:\Users\%username%\AppData\Local\Packages\
# PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\
# LocalCache\local-packages\Python311\site-packages'

import Graphene

#This is the data set that will be graphed
data1 = [5, 3, 1, 3, 5]

#Using the 'dot' function, add 3 arguments of
#the data set
#if connecting lines whould be drawn
#and the size of the dots
Graphene.dot(data1, False, 10)

#The first parameter is required
#The second parameter defaults to True
#The third parameter defaults to 15

#Using the 'bar' function, add 2 arguments of
#the data set
#and the size of the bars
Graphene.bar(data1, 15)

#The first parameter is required
#The second parameter defaults to 30

#This is the data set that will be graphed
data2 = [(1, 6), (2, 6), (1, 5), (2, 5), 
         (6, 6), (5, 6), (6, 5), (5, 5), 
         (3, 4), (4, 4), (2, 3), (3, 3), 
         (4, 3), (5, 3), (2, 2), (3, 2), 
         (4, 2), (5, 2), (2, 1), (5, 1)]

#Using the 'scatter' function, add 2 arguments of
#the data set
#and the size of the dots
Graphene.scatter(data2, 50)

#The first parameter is required
#The second parameter defaults to 15
