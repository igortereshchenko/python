#return list of list matrix
def create_matrix( width, heigth):

    return [[" "] * width for i in range(heigth)]




#return matrix that is copy of given 
def create_copy(matrix):
    width=len(matrix[0])
    heigth=len(matrix)
    copy_matrix=create_matrix(width, heigth)
    for i in range(heigth):
        for j in range(width):
            copy_matrix[i][j]=matrix[i][j]

    return copy_matrix
    
# marix list of list matrix    
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element,'',end='')
        print('')


def flip_horizontally(matrix):
    copy_matrix= create_copy(matrix)
    copy_matrix.reverse()

    return copy_matrix
    
def flip_vertically(matrix):
    copy_matrix= create_copy(matrix)
    for row in copy_matrix:
        row.reverse()

    return copy_matrix
    
def merge_vertically(matrix_top,matrix_bottom):
    return matrix_top+matrix_bottom


def merge_horizontally(matrix_left,matrix_right):
    picture_matrix=[]
    for i in range(len(matrix_left)):
        picture_matrix.append(matrix_left[i]+matrix_right[i])
        
    return picture_matrix




#return matrix with top left arrow
def build_arrow(size):
    picture_arrow_matrix=create_matrix( size, size)
    for i in range(size):
        picture_arrow_matrix[i][i]='*'
        picture_arrow_matrix[i][0]='*'
        picture_arrow_matrix[0][i]='*'
        
    return picture_arrow_matrix


def build_picture(half_heigth):
    
    picture_arrow_top_left=build_arrow(half_heigth)
    picture_arrow_top_rigth=flip_vertically(picture_arrow_top_left)
    
    picture_matrix_bottom=merge_horizontally(picture_arrow_top_rigth,picture_arrow_top_left)
    
    picture_matrix_top=flip_horizontally(picture_matrix_bottom)
    
    picture_matrix=merge_vertically(picture_matrix_top,picture_matrix_bottom)
    
    return picture_matrix
    
#----------------------------------------------------
half_heigth=int(input("Enter half height"))    

picture_matrix=build_picture(half_heigth)

print_matrix(picture_matrix)
