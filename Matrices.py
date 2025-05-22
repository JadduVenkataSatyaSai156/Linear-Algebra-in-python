#!/usr/bin/env python
# coding: utf-8

# In[5]:


# python program for finding the determinant of a square matrix
# user input for a11
p = int(input("Enter value for 1st element in 1st row : "))
# user input for a12
q = int(input("Enter value for 1st element in 2nd row : "))
# user input for a21
r = int(input("Enter value for 2nd element in 1st row : "))
# user input for a22
s = int(input("Enter value for 2nd element in 2nd row : "))
# Define a 2x2 matrix
matrix = [[p, q], [r, s]]
# Calculate the determinant manually
determinant_squarematrix = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
print("The matrix : ", matrix,"\nThe determinant of the matrix : ", determinant_squarematrix)


# In[10]:


# python program for calculating rank of a matrix
def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0
    
    # Step 1: Perform Gaussian Elimination to get the row echelon form
    for row in range(rows):
        # Find the pivot element in the current column
        if matrix[row][row] == 0:
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    # Swap rows if necessary
                    matrix[row], matrix[i] = matrix[i], matrix[row]
                    break
        
        if matrix[row][row] != 0:
            # Normalize the pivot row
            pivot = matrix[row][row]
            for col in range(cols):
                matrix[row][col] /= pivot
            
            # Eliminate all rows below the current row
            for i in range(row + 1, rows):
                factor = matrix[i][row]
                for j in range(cols):
                    matrix[i][j] -= factor * matrix[row][j]
    
    # Step 2: Count non-zero rows, which gives the rank
    for row in range(rows):
        if any(matrix[row][col] != 0 for col in range(cols)):
            rank += 1
    
    return rank
a = int(input("enter a11 : "))
b = int(input("enter a12 : "))
c = int(input("enter a13 : "))
d = int(input("enter a21 : "))
e = int(input("enter a22 : "))
f = int(input("enter a23 : "))
g = int(input("enter a31 : "))
h = int(input("enter a32 : "))
i = int(input("enter a33 : "))
square_matrix = [[a, b, c], [d, e, f], [g, h, i]]
print("Rank of the matrix (Gaussian Elimination):", gaussian_elimination(square_matrix))


# In[19]:


# python program for calculating multiplication of two square matrices
def square_matrix(matrix_a, matrix_b):
    matrix_a = [[int(a11), int(a12)],[int(a21),int(a22)]]
    matrix_b = [[int(b11),int(b12)],[int(b21),int(b22)]]
    matrix_axb = [[a11*b11 + a12*b21], [a11*b12 + a12*b22], [a21*b11 + a22*b21], [a21*b12 + a22*b22]]
    return matrix_a, matrix_b, matrix_axb
a_11 = int(input("enter a11: "))
a_12 = int(input("enter a12: "))
a_21 = int(input("enter a21: "))
a_22 = int(input("enter a22: "))
matrice_a = [[a_11,a_12],[a_21,a_22]]
b_11 = int(input("enter b11: "))
b_12 = int(input("enter b12: "))
b_21 = int(input("enter b21: "))
b_22 = int(input("enter b22: "))
matrice_b = [[b_11,b_12],[b_21,b_22]]
multiplication_matrix = square_matrix(matrice_a, matrice_b)
print(multiplication_matrix)

