from numbers import Number
import decimal
import copy

def dot_product(vector1, vector2):
    assert len(vector1) == len(vector2)
    prod = 0
    for n in range(len(vector1)):
        prod += vector1[n] * vector2[n]
    return prod

class MatrixError(Exception):
    pass

class Matrix(object):
    def __init__(self, *rows):
        for row in rows:
            assert len(row) == len(rows[0])
            for cell in row:
                assert isinstance(cell, Number)
        for m in range(len(rows)):
            for n in range(len(rows[0])):
                rows[m][n] = float(rows[m][n])
        self._rows = rows

    @classmethod
    def construct(cls, m, n, function):
        rows = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(function(i+1, j+1))
            rows.append(row)
        return cls(*rows)

    @classmethod
    def zero(cls, row_count, column_count):
        return cls.construct(row_count, column_count, lambda x, y: 0)

    @classmethod
    def identity(cls, row_count):
        return cls.construct(row_count, row_count, lambda x, y: 1 if x == y else 0)

    def __repr__(self):
        return "Matrix(*%r)" % (self._rows,)

    def row_count(self):
        return len(self._rows)

    def column_count(self):
        return len(self._rows[0])

    def rows(self):
        return copy.deepcopy(list(self._rows))

    def columns(self):
        cols = []
        for m in range(self.column_count()):
            col = []
            for n in range(self.row_count()):
                col.append(self.element(n+1,m+1))
            cols.append(col)
        return cols

    def row(self, i):
        if not isinstance(i, int):
            raise MatrixError, 'The row index must be an integer'
        if i > self.row_count() or i < 1:
            raise MatrixError, 'The row index is too large'
        return self.rows()[i-1]

    def column(self, j):
        if not isinstance(j, int):
            raise MatrixError, 'The column index must be an integer'
        if j > self.column_count():
            raise MatrixError, 'The column index is too large'
        return self.columns()[j-1]

    def element(self, m, n):
        return self.rows()[m-1][n-1]

    def equal_dimensions(self, other):
        return self.row_count() == other.row_count() and self.column_count() == other.column_count()

    def is_square(self):
        return self.row_count() == self.column_count()

    def element_function(self, function):
        return self.__class__.construct(self.row_count(), self.column_count(), lambda x,y: function(self.element(x, y)))

    def __eq__(self, other):
        if not self.equal_dimensions(other):
            return False
        for first, second in zip(self._rows, other._rows):
            if first != second:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if not self.equal_dimensions(other):
            raise MatrixError, 'The matrices do not have the same number of rows and columns'
        return self.__class__.construct(self.row_count(), self.column_count(), lambda x, y: self.element(x, y) + other.element(x, y))

    def __sub__(self, other):
        return self + other.scal(-1)

    def scal(self, number):
        return self.element_function(lambda x: number * x)

    def __mul__(self, other):
        if self.column_count() !=  other.row_count():
            raise MatrixError, 'The matrices cannot be multiplied'
        return self.__class__.construct(self.row_count(), other.column_count(), lambda x, y: dot_product(self.row(x), other.column(y)))

    def transpose(self):
        return self.__class__.construct(self.column_count(), self.row_count(), lambda x, y: self.element(y, x))

    def power(self, n):
        if not isinstance(n, int):
            raise MatrixError, 'The exponent must be an integer'
        prod = self.__class__.identity(self.row_count())
        if n >= 0:
            for k in range(n):
                prod *= self
            return prod
        for k in range(-1 * n):
            prod *= self.inverse()
        return prod

    def minor_matrix(self, i, j):
        if i > self.row_count() or j > self.column_count():
            raise MatrixError, 'One of the arguments is too large'
        rows = self.rows()
        del rows[i-1]
        for m in range(len(rows)):
            del rows[m][j-1]
        return self.__class__(*rows)

    def cofactor(self, i, j):
        return ((-1) ** (i + j)) * self.minor_matrix(i, j).det()

    def det(self):
        if not self.is_square():
            raise MatrixError, 'The matrix is not square'
        if self.row_count() == 1:
            return self.element(1, 1)
        else:
            determinant = 0
            for m in range(self.column_count()):
                determinant += self.element(1, m+1) * self.cofactor(1, m+1)
            return determinant

    def is_invertible(self):
        return self.det() != 0

    def adjugate(self):
        if not self.is_invertible():
            raise MatrixError, 'The matrix is not invertible'
        return self.__class__.construct(self.row_count(), self.row_count(), lambda x, y: self.cofactor(x, y)).transpose()

    def inverse(self):
        if not self.is_invertible():
            raise MatrixError, 'The matrix is not invertible'
        return self.adjugate().scal(1.0 / self.det())

    def is_symmetric(self):
        return self == self.transpose()

    def is_orthogonal(self):
        return self.transpose() == self.inverse()



