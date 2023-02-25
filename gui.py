import io
import sys
import os
from typing import TextIO
from pathlib import Path
import math
import re
from Calculator import *

def calculate_expression(expr):
    return Z7_num(eval(expr))

def create_matrix()

def interface(string, out):
    string = string.read()
    a = string.split()
    if a[0] == "calc":
        print(calculate_expression("".join(a[1:])), file=out)
    if a[0] == "exit":
        exit(0)
    if a[0] == "create" and a[1] == "matrix":


if __name__ == "__main__":
    print("$ ", end="")
    for line in sys.stdin:
        interface(io.StringIO(line), sys.stdout)
        print("$ ", end="")

