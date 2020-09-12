import numpy as np

a = 500
r = np.random.choice(a=a, size=50, replace=False, p=None)
print(a)
r1 = np.random.choice(a=a, size=50, replace=False, p=None)
print(a)
r2 = np.random.choice(a=a, size=50, replace=False, p=None)
print(a)
print(r)
print(r1)
print(r2)
