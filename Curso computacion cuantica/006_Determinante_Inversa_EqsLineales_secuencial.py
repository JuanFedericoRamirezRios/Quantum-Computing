"""
Ejecutar con python 3.10
"""

import numpy as np

# Programacion secuencial:

M = np.array([[-1,2,3,0],[0,1,-2,1],[3,-1,0,1],[2,1,0,-1]])
print(M, '\n')

print("Determinante=", end='')
print(np.linalg.det(M))
print()
print("Matriz inversa=")
print(np.linalg.inv(M))
print()
b=np.array([[1],[-1],[2],[-2]])
print(b, '\n')
print()
print("Solucion del sistema de ecuaciones:")
x = np.linalg.solve(M, b)
print(x)
print('a =', "{:.2E}".format(x[0][0]))
print('b =', "{:.2E}".format(x[1][0]))
print('c =', "{:.2E}".format(x[2][0]))
print('d =', "{:.2E}".format(x[3][0]))
print('comprobando solucion:', np.allclose(np.dot(M, x), b))
