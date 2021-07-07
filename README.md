# Regression-algorithms-ML

This is aa simple implementation of all the regression models used in Machine Learning using python.

___

## TABLE OF CONTENTS 

1.[Simple Linear Regression](#simple)  

2.[Multiple Linear Regression](#multiple)  

3.[Polynomial Regression](#polynomial)

4.[Support Vector Regression](#SVR)

___

## Simple Linear Regression <a name='Simple Linear Regression'></a>
Linear regression is the most widely used statistical technique; it is a way to model a relationship between two sets of variables. The result is a linear regression equation that can be used to make predictions about data.

```
y = b0 + b1*X
```

where,   
    y = dependant variable   
    X = independant variable  
    b1 = coefficient for independant variable  



### **Steps involved**
1. Importing the libraries.
2. Importing the datasets.
3. Splitting the dataset into training and tesing sets.
4. Training the simple linear regression model on training set.
5. Predicting the test results.
6. Visualizing both training and testing set.  

> *Note the dataset used for Simple Linear Regression is 'Data.csv'

___


## Multiple Linear Regression <a name='Multiple Linear Regression'></a>
Multiple Linear Regression is same as linear regression but it contains relationship between 2 or more sets of variables. 

```
y = b0 + b1*X1 + b2*X2 + ...... bn*Xn
```
### **Steps involved**
1. Importing the libraries.
2. Importing the datasets.
3. Encoding the categorical data.
4. Splitting the dataset into training and testing sets.
5. Training the multiple linear regression on the training set.
6. Prediction the results. 

> *Note the dataset used for Multiple Linear Regression is '50_Startups.csv'

___

## Polynomial regression
Polynomial regression is a form of regression analysis in which the relationship between the independent variable x and the dependent variable y is modelled as an nth degree polynomial in x. It is a special type of multiple linear regression.

```
y = b0 + b1*X1 + b2*X2^2 + b3*X3^3 + ..... bn*Xn^n
```
### **Steps involved**
1. Importing the libraries.
2. Importing the dataset.
3. Training linear regression on the dataset.
4. Training the polynomial regression the dataset.
5. Visualizing the linear regression model.
6. Visualizing the polynomial regression model. 
7. Predicting a new result using linear regression.
8. Predicting a new result using polynomial regression. 

> *Note the dataset used for Polynomial Regression is "Position_Salaries.csv"

___

## Support Vector Regression (SVR)  <a name='Support Vector Regression'></a>
SVR is a powerful algorithm that allows us to choose how tolerant we are of errors, both through an acceptable error margin(ϵ) and through tuning our tolerance of falling outside that acceptable error rate. Instead of a simple line, it takes a tube of width epsilon(ϵ) which is an intensive tube.

```
y=1/2 |(|w|)|^2+c∑_(i=1)^M▒〖(ξ+ ξ_i^* )→MIN〗
```   
### **Steps involved**
1. Importing the libraries.
2. Importing the datasets.
3. Feature Scaling
4. Training the SVR models on the whole training set.
5. Predicting a new result.
6. Visualizing the SVR results.

> *Note Datasets are not split to leverage maximum data to extract max correlation between position and salary. The dataset used is 'Position_Salaries.csv'. Feature scaling is required before traing as SVR has implicit equation/relationship.   

> *Note for Linear SVR we use Linear Kernel similarly for non linear we use Non Linear Kernel 


