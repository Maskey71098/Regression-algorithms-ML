#IMPORTING THE LIBRARIES

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

#IMPORTING THE DATASET

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
#transforming y to 2d array
y = y.reshape(len(y),1)


#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
X = sc_x.fit_transform(X)
y = sc_y.fit_transform(y)
print(X)
print(y)

#TRAINING THE WHOLE DATASET ON SVR
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)

#PREDICTIONG A NEW RESULT
result = sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]])))
#print(result)
#170370

#VISUALIZING THE RESULT
plt.scatter(sc_x.inverse_transform(X), sc_y.inverse_transform(y), color='red')
plt.plot(sc_x.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color='blue')
plt.title('SVR')
plt.xlabel('position')
plt.ylabel('salary')
plt.show()

#VISUALIZING THE RESULT IN HIGHER RESOLUTION
X_grid = np.arange(min(sc_x.inverse_transform(X)), max(sc_x.inverse_transform(X)), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_x.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(X_grid, sc_y.inverse_transform(regressor.predict(sc_x.transform(X_grid))), color = 'blue')
plt.title('SVR')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
