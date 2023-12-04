#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = 0
    while n < 3:
        if matrix[n] == []:
            print()
            break
        else:
            p = 0
            while p < 3:
                print("{}".format(int(matrix[n][p])), end=" ")
                p += 1
        print()
        n += 1
#   for i in matrix:
 #       remove = str.maketrans({"[": "", "]": "", ",": " "})
  #      matrix = str(i).translate(remove)
   #     print("{}".format(int(matrix))) 
