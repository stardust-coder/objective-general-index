import numpy as np
import pandas as pd

def solve_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

def coord_descent(weight,matrix,index):
    '''
    matrix: numpy array (n x n)
    weight: numpy array (n x 1)
    '''
    i = index
    s = matrix[i]@weight
    s -= matrix[i][i] * weight[i][0]
    a = matrix[i][i]
    b = s
    c = -1
    wi, _ = solve_quadratic_equation(a,b,c)
    assert wi > 0
    weight[i][0] = wi
    return weight


def ogi_weight(data, is_csv=False):
    '''
    data: data matrix (d x n)
    '''
    if is_csv:
        data = pd.read_csv(data).values.T
    print("Data matrix:")
    print(data)
    
    covar = np.cov(data, bias=True) #dxd
    print("Covariance matrix:")
    print(covar)

    d = len(data)
    weight = np.ones((d,1))
    k = 0
    while True:
        tmp = weight.copy()
        k += 1
        print(f"Iteration {k}")
        print("Current Weight")
        print(weight)
        for i in range(d):
            weight = coord_descent(weight,covar,i)
        if abs(np.sum(tmp-weight)) < 1e-5:
            print("Final weight")
            print(weight)
            break
    g = weight.T@data
    vectors = [weight[j][0]*data[j] for j in range(d)]
    print("OGI weighted data:")
    print(vectors)
    print("OGI:")
    print(g[0])
    return weight, vectors, g[0]


if __name__ == "__main__":
    data = "data/sample.csv"
    ogi_weight(data, True)