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
    def zero(cls, row_count, column_count):
        rows = []
        for m in range(row_count):
            row = []
            for n in range(column_count):
                row.append(0)
            rows.append(row)
        return cls(*rows)

    def __repr__(self):
        return "Matrix(*%r)" % (self._rows,)

    @classmethod
    def identity(cls, row_count):
        rows = []
        for m in range(row_count):
            row = []
            for n in range(row_count):
                if m == n: row.append(1)
                else: row.append(0)
            rows.append(row)
        return cls(*rows)

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

    def element(self, m, n):
        return self.rows()[m-1][n-1]

    def equal_dimensions(self, other):
        return self.row_count() == other.row_count() and self.column_count() == other.column_count()

    def is_square(self):
        return self.row_count() == self.column_count()

    def element_function(self, function):
        rows = []
        for m in range(self.row_count()):
            row = []
            for n in range(self.column_count()):
                row.append(function(self.element(m+1,n+1)))
            rows.append(row)
        return Matrix(*rows)

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
        rows = []
        for m in range(self.row_count()):
            row = []
            for n in range(self.column_count()):
                row.append(self.element(m+1, n+1) + other.element(m+1, n+1))
            rows.append(row)
        return Matrix(*rows)

    def __sub__(self, other):
        return self + other.scal(-1)

    def scal(self, number):
        return self.element_function(lambda x: number * x)

    def __mul__(self, other):
        if self.column_count() !=  other.row_count():
            raise MatrixError, 'The matrices cannot be multiplied'
        rows = []
        for m in range(self.row_count()):
            row = []
            for n in range(other.column_count()):
                row.append(dot_product(self.rows()[m], other.columns()[n]))
            rows.append(row)
        return Matrix(*rows)

    def transpose(self):
        rows = []
        for m in range(self.column_count()):
            row = []
            for n in range(self.row_count()):
                row.append(self.element(n+1,m+1))
            rows.append(row)
        return Matrix(*rows)

    def power(self, n):
        if not isinstance(n, int):
            raise MatrixError, 'The exponent must be an integer'
        prod = Matrix.identity(self.row_count())
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
        return Matrix(*rows)

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
        rows = []
        for m in range(self.row_count()):
            row = []
            for n in range(self.row_count()):
                row.append(self.cofactor(m+1, n+1))
            rows.append(row)
        return Matrix(*rows).transpose()

    def inverse(self):
        if not self.is_invertible():
            raise MatrixError, 'The matrix is not invertible'
        return self.adjugate().scal(1.0 / self.det())



