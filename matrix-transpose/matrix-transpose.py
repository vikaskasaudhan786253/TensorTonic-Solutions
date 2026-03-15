import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    if np.shape(A)[0]==np.shape(A)[1]:
        for i in range(np.shape(A)[0]):
            for j in range(np.shape(A)[1]):
                if i<j:
                    A[i][j],A[j][i] = A[j][i],A[i][j]
        return A
    else:
        arr = np.zeros((np.shape(A)[1],np.shape(A)[0]))
        for i in range(np.shape(A)[0]):
            for j in range(np.shape(A)[1]):
                arr[j][i] = A[i][j]
        return arr