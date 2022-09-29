# print reversed triangle; input # of rows

"""
ex: 12 rows
0  1  2  3  4  5  6  7  8  9  10 11 10 9  8  7  6  5  4  3  2  1  0  
   0  1  2  3  4  5  6  7  8  9  10 9  8  7  6  5  4  3  2  1  0  
      0  1  2  3  4  5  6  7  8  9  8  7  6  5  4  3  2  1  0  
         0  1  2  3  4  5  6  7  8  7  6  5  4  3  2  1  0  
            0  1  2  3  4  5  6  7  6  5  4  3  2  1  0  
               0  1  2  3  4  5  6  5  4  3  2  1  0  
                  0  1  2  3  4  5  4  3  2  1  0  
                     0  1  2  3  4  3  2  1  0  
                        0  1  2  3  2  1  0  
                           0  1  2  1  0  
                              0  1  0  
                                 0  

"""

rows = int(input("Enter number of rows: "))

# old versions:
#v.1
# for i in range(rows, 0, -1):
#     elms = 2*i-1
#     for space in range(0, rows-i):
#         print("  ", end="")
#     for j in range(0, i):
#         print(f"{j} ", end="")
#     for j in range(i, elms):
#         print(f"{elms -j -1} ", end="")
    
#     print()
 
#v.2   
# for pos, i  in enumerate(range(rows, 0, -1)):
#     elms = 2*i-1
#     for space in range(0, pos):
#         print("  ", end="")
#     for j in range(0, i):
#         print(f"{j} ", end="")
#     for j in range(i, elms):
#         print(f"{elms -j -1} ", end="")
    
#     print()
  
#v.3  
# for row in range(0, rows):
#     print("  " * row, end="")
#     for n in range(0, rows-row):
#         print(f"{n} ", end="")
#     for n in range(rows-1-row-1, -1, -1):
#         print(f"{n} ", end="")
        
#     print()
  
# best version  
#v.4
sp_width = 2 if rows < 10 else 3 
spaces =  " " * sp_width

for row_no in range(rows):
    print(spaces * row_no, end="") 
    for n in range(rows - row_no):
        print(f"{n:<{sp_width}}", end="")
    for n in range(rows-1 - row_no - 1, -1, -1):
        print(f"{n:<{sp_width}}", end="")
        
    print()
        
