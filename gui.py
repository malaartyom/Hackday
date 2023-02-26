import io
import sys
import os
from typing import TextIO
from pathlib import Path
from Calculator import *

VALUES = dict()

def calculate_expression(expr):
    return Z7_num(eval(expr))

def create_matrix_from_file(pathname):
    pathname = os.path.abspath(pathname)
    f = open(pathname, "r")
    file = f.read()
    matrix = Z7_Matrix(len([[int(j) for j in i.split()] for i in file.splitlines()]),[[int(j) for j in i.split()] for i in file.splitlines()])
    return matrix

def interface(string, out):
    string = string.read()
    a = string.split()
    if len(a) == 0:
        print("If you need help type 'help'", file=out)
    elif a[0] == "help":
        # if a[1][5:] != "Russian":
        #     print("If you want to read manual on other language enter:' help lang=perferable language' ")
        #     print("Basic language is English")
        #     print("There are two avalible language optinos: English and Russian")
        # else:
        #     print("Если вы хотите читать документацию на другогм языке введите: 'help lang=препдпочтит'")
        s = "To read a matrix from a file and store it in a variable M enter: create matrix file=[pathname] as [M]"
        print(len(s) * "-")
        print()
        print("To calculate some expressions into Z7 field use command 'calc [some expression]'")
        print("For example:")
        print("calc 2 * 5")
        print("3")
        print()
        print(len(s) * "-")
        print()
        print("To exit programm enter: exit")
        print()
        print(len(s) * "-")
        print()
        print(s)
        print("Where pathname is the name of the path to the file")
        print(len(s) * "-")
        print()
        print("To print a matrix enter: print [M]")
        print("Where M is the variable in which the matrix is written")
        print()
        print(len(s) * "-")
        print()
        print("To calculate determinant of the matrix enter: det [M]")
        print("Where M is the variable in which the matrix is written")
        print()
        print(len(s) * "-")
        print()
        print("To transpose matrix use comand: transpose [M]")
        print("Where M is the variable in which the matrix is written")
        print()
        print(len(s) * "-")
        print()
        print("To make elementary transoformations of the first type of the matrix M enter:")
        print("transform [M] 1 [line1] [line2]")
        print("Where line1 and line2 are the lines that we want to swap")
        print()
        print(len(s) * "-")
        print()
        print("To make elementary transoformations of the third type of the matrix M enter:")
        print("transform [M] 3 [line1][const][line2]")
        print("If you want to add line1 multiplied by const to line2")
        print()
        print(len(s) * "-")
        print()
        print("Use command: mlt [M1] [M2] to calculate M1 multuplied by M2")
        print("Where M1 and M2 are variables in which the matrices are written ")
        print()
        print("Use command: mlt [M1] [M2] as [M3] to calculate M1 multuplied by M2")
        print("And write the answer into variable M3")
        print("Where M1 and M2 are variables in which the matrices are written ")
        print()
        print(len(s) * "-")
        print()
        print("To superdiagonalise matrix M use command: diag [M]")
        print(f"To superdiagonalise matrix M and make the same transformatin with matrix E use command: diag [M] with E")
        print("Where M is the variable in which the matrix is written")
        print()
        print(len(s) * "-")
    elif a[0] == "calc":
        print(calculate_expression("".join(a[1:])), file=out)
    elif a[0] == "exit":
        exit(0)
    elif a[0] == "create":
        if a[1] == "matrix":
            if a[2][:4] == "file":
                pathname = a[2][5:]
                VALUES[str(a[-1])] = create_matrix_from_file(pathname)
        elif a[2] == "num":
            pass
    elif a[0] == "print":
        print(VALUES[a[1]], file=out)
    elif a[0] == "transform":
        if a[1] == "3":
            matrix = VALUES[str(a[2])]
            line1 = int(a[3])
            const = Z7_num(int(a[4]))
            line2 = int(a[5])
            matrix.elementary_transformation_3(line1, const, line2)
            VALUES[str(a[2])] = matrix
        elif a[1] == "2":
            print(" :( :( Sorry this type of transformation is not realised......")
        elif a[1] == "1":
            matrix = VALUES[str(a[2])]
            line1 = int(a[3])
            line2 = int(a[4])
            matrix.elementary_transformation_1(line1, line2)
            VALUES[str(a[2])] = matrix
    elif a[0] == "det":
        matrix = VALUES[str(a[1])]
        print(matrix.determinant(), file=out)
    elif a[0] == "transpose":
        VALUES[str(a[1])].transpose()
    elif a[0] == "diag":
        if "with" not in a:
            VALUES[str(a[1])].superdiegonolise()
        else:
            ret = VALUES[str(a[1])].superdiegonolise()
            E = Z7_Matrix(VALUES[str(a[1])].size, 1)
            E.make_transformations(ret)
            print("-" * (2 * E.size - 1))
            print(VALUES[str(a[1])])
            print("-" * (2 * E.size - 1))
            print(E)
            print("-" * (2 * E.size - 1))
    elif a[0] == "mlt":
        if "as" not in a:
            print(VALUES[a[1]] * VALUES[a[2]], file=out)
        else:
            VALUES[a[-1]] = VALUES[a[1]] * VALUES[a[2]]

# create matrix file=/Users/artemmalarenko/Documents/GitHub/Hackday/test.txt as M1
if __name__ == "__main__":
    print("$ ", end="")
    for line in sys.stdin:
        interface(io.StringIO(line), sys.stdout)
        print("$ ", end="")

