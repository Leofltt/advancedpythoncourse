squares = [0,1,4,9,16,25]

# list comprehension
squares_lc = [x**2 for x in range(6)]

# filter only squares for even numbers
squares_lc_even = [x**2 for x in range(6) if x % 2 == 0]

# returning whether numbers are even or odd
even_or_odd = ['even' if x % 2 == 0 else 'odd' for x in range(6)]

# nested list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix_lc = [[row[i] for row in matrix] for i in range(3)]

matrx = [[i+j for j in range(3)] for i in range(1,4)]

print(matrx)