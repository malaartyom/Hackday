import io
import sys
import os
from typing import TextIO
from pathlib import Path
import math
import re
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

