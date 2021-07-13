# Regression-algorithms-ML

This is aa simple implementation of all the regression models used in Machine Learning using python.

___

## TABLE OF CONTENTS 

1.[Simple Linear Regression](##Simple-Linear-Regression)  

2.[Multiple Linear Regression](#Multiple-Linear-Regression)  

3.[Polynomial Regression](##Polynomial-Regression)

4.[Support Vector Regression](##Support-Vector-Regression-(SVR))   

5.[Decision Tree Regression](##Decision-Tree-Regression)

6.[Random Forest Regression](##Random-Forest-Regression)   

___

## Simple Linear Regression 
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

## Polynomial Regression
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

___   
 
## Decision Tree Regression <a name='Decision Tree Regression'></a>  
 Decision tree builds regression model in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes.

 ### **Steps involved**   
 1. Import the libraries.
 2. Import the dataset.
 3. Train the dataset on the regression model.
 4. Predicting the results.
 5. Visualizing the results in a high resolution plot(using grids).

 > *Note Feature Scaling is not required for decision tree as they are not sensitive to variance changes.

 > *Note the dataset used for decision tree regression is 'Position_Salaries.csv'

 ### **Observation**
 The decision tree regression done on 2-D datasets don't produce good prediction as they require more than one independent variables to better predict  the dependant variable.
___   

## Random Forest Regression <a name='Random Forest Regresion'></a>   

Random Forest Regression is a supervised learning algorithm that uses ensemble learning method for regression. A Random Forest operates by constructing several decision trees during training time and outputting the mean of the classes as the prediction of all the trees.   
 
 >*Note decision tree regression and random forest regression are almost similar to eachother. In random tree regression, it predicts a forest of trees as oposed to decision tree regresssion which predicts only one tree. 

 >Feature scaling is not required

### **Steps involved**  
 1. Import the libraries.
 2. Import the dataset.
 3. Train the dataset on the regression model.
 4. Predicting the results.
 5. Visualizing the results in a high resolution plot(using grids).

> *Note the dataset used for decision tree regression is 'Position_Salaries.csv'

___

## **Evalutation of models**    
Performance of each regression algortihm was tested by implying it on 'Data.csv' dataset. The values of the evaluation are as follows:

| S.N     | Model    | Evaluation value    |
| :------------- | :----------: | -----------: |
|  1. | Multiple Regression  | 0.9325315554761303   |
|  1. | Polynomial Regression  | 0.9458193300146379   |
|  1. |SVR  | 0.948078404998626   |
|  1. | Decision Tree Regression   | 0.922905874177941    |
| 2.  | Random Forest Regression | 0.948078404998626 |
