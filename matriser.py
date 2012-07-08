# Matriseoperasjoner

def is_vector(liste):
    for k in range(0, len(liste)):
        if not (isinstance(liste[k], float) or isinstance(liste[k], int)):
            return False
    return True

def is_matrix(liste):
    if is_vector(liste):
        return True
    for k in range(0, len(liste)):
        if is_vector(liste[k]) == False:
            return False
        if k > 0:
            if len(liste[k-1]) != len(liste[k]):
                return False
    return True
            
print is_matrix([1, 2.3])
print is_matrix([1.0,3.0,2.5])
print is_matrix([[1.0,0.0],[1.3,2.9,3.6]])
print is_matrix([[2.3,4.5],[7.5,1.9]])
print is_matrix([[1,0,1],[0,0,1],[1,0,2],[2,0,3],[1,0,4]])

def matrix_sum(matrix1, matrix2):
    if not (is_matrix(matrix1) and is_matrix(matrix2)):
        print 'matrisene er ikke gyldige'
        return
    if not ((len(matrix1) == len(matrix2)) and (len(matrix1[0]) == len(matrix2[0]))):
        print 'matrisene har forskjellig stoerrelse'
        return
    
    matrix = []
    for m in range(0, len(matrix1)):
        rad = []
        for n in range(0, len(matrix1[0])):
            rad.append(matrix1[m][n] + matrix2[m][n])
        matrix.append(rad)
    return matrix

print matrix_sum([[1,0],[0,1]],[[0,1],[1,0]])
