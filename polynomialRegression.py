#IMPORTING THE LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IMPORTING THE DATASET

dataset = pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:, 1:-1].values
y=dataset.iloc[:, -1].values

#TRAINING LINEAR REGRESSION ON WHOLE DATASET

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#TRAINING POLYNOMIAL REGRESSION ON WHOLE DATASET

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#VISUALIZING THE LINEAR REGRESSION RESULTS

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#VISUALIZING THE POLYNOMIAL REGRESSION RESULTS

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('True or False Salary(Polynomial Regression)')
plt.xlabel('position')
plt.ylabel('salary')
plt.show()

#VISUALIZIN THE POLYNOMIAL REGRESSION RESULTS
#FOR HIGHER RESOLUTION AND SMOOTHER CURVE
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#PREDICTION A NEW RESULT USING POLYNOMIAL REGRESSION
salary = lin_reg.predict([[6.5]])   #[[]] 2d array
#salary = 330379

#PREDICTION A NEW RESULT USING POLYNOMIAL REGRESSION
salary_poly = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
#salary =158862
