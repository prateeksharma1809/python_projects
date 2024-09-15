import numpy as np

def test():
    X = np.array([[1, 6,5], [1,5, 6],[1,4,3],[1,3,4],[1,2,3],[1,3,2]])
    y = np.array([1,0,1,0,0,1])
    print('====y====')
    print(y)
    print('====X====')
    print(X)
    print('====X.T====')
    print(X.T)
    print('====X.T @ X====')
    print(X.T @ X)
    print('====np.linalg.inv(X.T @ X)====')
    print(np.linalg.inv(X.T @ X))
    print('====beta====')
    beta = np.linalg.inv(X.T @ X) @ X.T @ y
    print(beta)

test()