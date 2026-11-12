import numpy as np
x = np.array([30, 40, 50, 60])    
y = np.array([1.5, 2.0, 2.5, 3.0])
#(X^TX)^-1X^Ty
X = np.c_[np.ones(len(x)), x]
W = np.linalg.inv(X.T @ X) @ X.T @ y
print(W)