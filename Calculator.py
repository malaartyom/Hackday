class Z7_num:

    def __init__(self, num: int):
        if num >= 0:
            self.value = num % 7
        else: 
            self.value = 7 - ((-num) % 7)
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __add__(self, other):
        return Z7_num(self.value + other.value)

    def __mul__(self, other):
        return Z7_num(self.value * other.value)
    
    def __sub__(self, other):
        return Z7_num(self.value - other.value)
    
    def __neg__(self):
        return Z7_num(-self.value)


class Z7_Matrix:
    
    def __init__(self, num, *args):
        self.size = num
        self.value = [[Z7_num(0) for i in range(num)] for j in range(num)]

        if args:
            for i in range(self.size):
                for j in range(self.size):
                    self.value[i][j] = args[i][j]
    
    def __str__(self) -> str:
        return_string = ""
        for i in range(self.size):
            for j in range(self.size):
                return_string += Z7_num.__str__(self.value[i][j])
                return_string += " "
            return_string += "\n"
        return return_string[:-1]


if __name__ == "__main__":
    A = Z7_Matrix(3)
    print(A)
