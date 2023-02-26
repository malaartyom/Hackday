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
    if a[0] == "help":
        # if a[1][5:] != "Russian":
        #     print("If you want to read manual on other language enter:' help lang=perferable language' ")
        #     print("Basic language is English")
        #     print("There are two avalible language optinos: English and Russian")
        # else:
        #     print("Если вы хотите читать документацию на другогм языке введите: 'help lang=препдпочтит'")
        s = "To read a matrix from a file and store it in a variable M enter: create matrix file=[pathname] as [M]"
        print(len(s) * "-")
        print("To calculate some expressions into Z7 field use command 'calc [some expression]'")
        print("For example:")
        print("calc 2 * 5")
        print("3")
        print(len(s) * "-")
        print("To exit programm enter: exit")
        print(len(s) * "-")
        print(s)
        print("Where pathname is the name of the path to the file")
        print(len(s) * "-")
        print("To print a matrix enter: print [M]")
        print("Where M is the variable in which the matrix is written")
        print(len(s) * "-")
        print("To calculate determinant of the matrix enter: det [M]")
        print("Where M is the variable in which the matrix is written")
        print(len(s) * "-")
        print("To transpose matrix use comand: transpose M")
        print("Where M is the variable in which the matrix is written")
        print(len(s) * "-")
        print("To make elementary transoformations of the first type of the matrix M enter:")
        print("transform [M] 1 [line1] [line2]")
        print("Where line1 and line2 are the lines that we want to swap")
        print(len(s) * "-")
        print("To make elementary transoformations of the third type of the matrix M enter:")
        print("transform [M] 3 [line1][const][line2]")
        print("If you want to add line1 multiplied by const to line2")
        print(len(s) * "-")
    if a[0] == "calc":
        print(calculate_expression("".join(a[1:])), file=out)
    if a[0] == "exit":
        exit(0)
    if a[0] == "create":
        if a[1] == "matrix":
            if a[2][:4] == "file":
                pathname = a[2][5:]
                VALUES[str(a[-1])] = create_matrix_from_file(pathname)
        elif a[2] == "num":
            pass
    if a[0] == "print":
        print(VALUES[a[1]], file=out)
    if a[0] == "transform":
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
    if a[0] == "det":
        matrix = VALUES[str(a[1])]
        print(matrix.determinant(), file=out)
    if a[0] == "transpose":
        VALUES[str(a[1])].transpose()
# /Users/artemmalarenko/Documents/GitHub/Hackday/1.txt

if __name__ == "__main__":
    print("$ ", end="")
    for line in sys.stdin:
        interface(io.StringIO(line), sys.stdout)
        print("$ ", end="")

