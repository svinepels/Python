import unittest
from matrix import Matrix, MatrixError

class MatriserTest(unittest.TestCase):
    def testColumns(self):
        matrix = Matrix([1, 3, 4], [-3, 2.5, 8], [3, 6, 1], [3, 0, 5])
        self.assertEquals(
            matrix.rows(),
            [[1, 3, 4], [-3, 2.5, 8], [3, 6, 1], [3, 0, 5]])
        self.assertEquals(
            matrix.columns(),
            [[1, -3, 3, 3], [3, 2.5, 6, 0], [4, 8, 1, 5]])
    
    def testSum(self):
        matrix1 = Matrix([2,1],[3,5])
        matrix2 = Matrix([4,7],[6,0])
        self.assertEquals(
            Matrix([6, 8], [9, 5]),
            matrix1 + matrix2)
    
    def testEquality(self):
        self.assertEquals(
            Matrix([1,0],[0,1]),
            Matrix([1,0],[0,1]))

    def testSumDifDim(self):
        matrix1 = Matrix([1,0], [0,1])
        matrix2 = Matrix([1,0], [2,3], [4,3])
        self.assertRaises(
            MatrixError,
            lambda: matrix1 + matrix2)

    def testEqualityChecksRowLength(self):
        self.assertNotEqual(
            Matrix([1, 1]),
            Matrix([1, 1], [0, 0]))

    def testMatricesOnlyNumbers(self):
        self.assertRaises(
            AssertionError,
            lambda: Matrix(['a',1], [0,1]))

    def testNumMult(self):
        matrix = Matrix([1, 1], [1, 1])
        self.assertEquals(
            Matrix([2, 2], [2, 2]),
            matrix.scal(2))

    def testTranspose(self):
        matrix = Matrix([1, 2], [3, 4])
        self.assertEquals(
            Matrix([1, 3], [2, 4]),
            matrix.transpose())
        matrix2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
        self.assertEquals(
            Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9]),
            matrix2.transpose())

    def testMult(self):
        matrix1 = Matrix([1, 0], [0, 1])
        matrix2 = Matrix([2, 5], [7, -3])
        self.assertEquals(
            matrix2,
            matrix1 * matrix2)
        matrix3 = Matrix([0, 4, 2], [3, 7, 3], [0, 1, 1], [4, 7, 7])
        matrix4 = Matrix([1, 2], [0, 5], [4, 8])
        self.assertEquals(
            matrix3 * matrix4,
            Matrix([8, 36], [15, 65], [4, 13], [32, 99]))

    def testElement(self):
        matrix = Matrix([1, 0, 3], [3, 5, 6])
        self.assertEquals(
            matrix.element(2, 2),
            5)

    def testPower(self):
        matrix = Matrix([2, 0], [0, 2])
        self.assertEquals(
            matrix.power(1),
            matrix)
        self.assertEquals(
            matrix.power(3),
            Matrix([8, 0], [0, 8]))

    def testZeroMatrix2(self):
        self.assertEquals(
            Matrix([0, 0, 0], [0, 0, 0]),
            Matrix.zero(2, 3))

    def testIdentityMatrix(self):
        self.assertEquals(
            Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1]),
            Matrix.identity(3))

    def testCofactor(self):
        self.assertEquals(
            Matrix([1, 3, 7, 0], [0, 0, 4, 3], [-3, 3, -9, 8], [2, 2, 0, 4.5]).minor_matrix(2, 3),
            Matrix([1, 3, 0], [-3, 3, 8], [2, 2, 4.5]))
        self.assertEquals(
            Matrix([1, 0], [0, 1]).minor_matrix(1, 1),
            Matrix([1]))
        self.assertEquals(
            Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1]).minor_matrix(1, 2),
            Matrix([0, 0], [0, 1]))
            

    def testIsSquare(self):
        self.assertEquals(
            Matrix([1]).is_square(),
            True)

    def testDeterminant(self):
        self.assertEquals(
            5,
            Matrix([5]).det())
        self.assertEquals(
            1,
            Matrix([1, 0], [0, 1]).det())
##        self.assertEquals(
##            1,
##            Matrix.identity(4).det())

unittest.main()
