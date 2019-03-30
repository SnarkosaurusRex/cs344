'''
This module works with the Boston Housing Dataset in pandas form

Dataset column descriptions:
      crim:       per capita crime rate by town
      zn:         proportion of residential land zoned for lots over 25,000 sq.ft
      indus:      proportion of non-retail business acres per town
      chas:       Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
      nox:        nitrogen oxides concentration (parts per 10 million)
      rm:         average number of rooms per dwelling
      age:        proportion of owner-occupied units built prior to 1940
      dis:        weighted mean of distances to five Boston employment centres
      rad:        index of accessibility to radial highways
      tax:        full-value property-tax rate per $10,000
      ptratio:    pupil-teacher ratio by town
      b:          1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
      lstat:      lower status of the population (percent)
      medv:       median value of owner-occupied homes in $1000s

@author ljh27
Spring 2019
'''

import pandas
import numpy


#load in the data
boston_df = pandas.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
print(boston_df.head())

#2a - print dimensions
print('Count: {}'.format(len(boston_df)))
print('Dimensions: {}'.format(boston_df.ndim))
print('Shape: {}'.format(boston_df.shape))
print('Data Types: \n{}'.format(boston_df.dtypes))

print("\n\n-----------------------")

#2b - split the dataset into training, testing, and validation sets
#shuffle the data first
boston_df = boston_df.reindex(numpy.random.permutation(boston_df.index))
print(boston_df.head())

trainingSet = boston_df[:380]
validationSet = boston_df[380:440]
testSet = boston_df[440:]

print('\nTrain Count: {}'.format(len(trainingSet)))
print('Dimensions: {}'.format(trainingSet.ndim))
print('Validation Count: {}'.format(len(validationSet)))
print('Dimensions: {}'.format(validationSet.ndim))
print('Test Count: {}'.format(len(testSet)))
print('Dimensions: {}'.format(testSet.ndim))


#2c - synthetic feature: if dis below avg and rad below avg
boston_df["prox"] = (boston_df["dis"] < boston_df["dis"].mean()) & (boston_df["rad"] < boston_df["rad"].mean())
print(boston_df)

