import numpy as np

x = np.array([30, 40, 50, 60])    
y = np.array([-1, 1, -1, 1])

w = 0.0
b = 0.0

m = len(x) 
epoch = 1  

while True:
    errors = 0 
    
    for i in range(m):
        s_i = y[i] * (w * x[i] + b)
        
        if s_i <= 0:
            w = w + y[i] * x[i]
            b = b + y[i]
            errors += 1
            
    print(f"Vòng {epoch} - Lỗi: {errors} | w: {w}, b: {b}")
    epoch += 1
    
    if errors == 0:
        break

print(f"w = {w}, b = {b}")