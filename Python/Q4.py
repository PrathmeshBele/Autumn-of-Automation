import numpy as np 

X = np.random.normal(0, 1, size=(20, 20))
y = np.random.randint(-1000,1000, (20,1)).astype('int32') # random integers from -1000 to 1000 


ans = np.linalg.pinv(X).dot(y)

print(ans)