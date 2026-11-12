import numpy as np
#w_t+1=w_t-eta*daoham
#loss=1/2m*sigma((w_0+w_1x-y)^2)
#w_0=w_0-eta*1/m(w_0+w_1x-y)
#w_1=w_1-eta*1/m(w_0+w_1x-y)*x
x = np.array([30, 40, 50, 60])    
y = np.array([1.5, 2.0, 2.5, 3.0])

w_0 = 0
w_1 = 0
eta = 0.0001
m = len(x)

for i in range(10000):
    y_hat = w_0 + w_1 * x
    loss = (1/(2*m)) * np.sum((y_hat - y) ** 2)
    w_0 = w_0 - eta * (1/m) * np.sum(y_hat -y)
    w_1 = w_1 - eta * (1/m) * np.sum((y_hat - y) * x)
    print(f"Loss: {loss}, w_0: {w_0}, w_1: {w_1}")
