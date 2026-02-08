"""
Ejecutar con python 3.10
"""

import numpy as np

class RES_EQS():

    def __init__(self, matrizCoef, vectInd):
        self.M = matrizCoef
        self.b = vectInd

    def Calc(self):
        print("Determinante=", end='')
        print(np.linalg.det(self.M))

        print("Matriz inversa=")
        print(np.linalg.inv(self.M))

        print("Solucion del sistema de ecuaciones:")
        x = np.linalg.solve(self.M, self.b)
        print(x)
        print('a =', "{:.2E}".format(x[0][0]))
        print('b =', "{:.2E}".format(x[1][0]))
        print('c =', "{:.2E}".format(x[2][0]))
        print('d =', "{:.2E}".format(x[3][0]))
        print('comprobando:', np.allclose(np.dot(self.M, x), self.b))


if __name__ == "__main__" :
    M1 = np.array([[-1,2,3,0],[0,1,-2,1],[3,-1,0,1],[2,1,0,-1]])
    print(M1, '\n')
    b1 = np.array([[1],[-1],[2],[-2]])
    print(b1, '\n')
    objeto1 = RES_EQS(matrizCoef=M1, vectInd=b1)
    objeto1.Calc()

    print('\n\nCon obteto2:')
    M2 = np.array([[-1j,2,3,0],[0,1j,-2,1],[3,-1,0,1],[2,1,0,-1j]])
    print(M2, '\n')
    b2=np.array([[1j],[-1],[2],[-2]])
    print(b2, '\n')
    objeto2 = RES_EQS(matrizCoef=M2, vectInd=b2)
    objeto2.Calc()
