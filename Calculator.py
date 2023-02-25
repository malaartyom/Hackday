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
    
    def __int__(self):
        return self.value


class Z7_Matrix:
    
    def __init__(self, num, *args):
        self.size = num
        self.value = [[Z7_num(0) for i in range(num)] for j in range(num)]

        if args:
            for i in range(self.size):
                for j in range(self.size):
                    self.value[i][j] = Z7_num(args[i][j])
    

    def __str__(self) -> str:
        return_string = ""
        for i in range(self.size):
            for j in range(self.size):
                return_string += Z7_num.__str__(self.value[i][j])
                return_string += " "
            return_string += "\n"
        return return_string[:-1]


    def copy(self):
        # This function make deep copy of matrix
        copied = Z7_Matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                copied.value[i][j] = Z7_num(int(self.value[i][j]))

        return copied


    def elementary_transformation_3(self, first_line_number: int, const: Z7_num, second_line_number: int):
        # This function make elementary transformation: add first line multiplied by const to second line

        first_line_number -= 1
        second_line_number -= 1

        for i in range(self.size):
            self.value[second_line_number][i] = self.value[first_line_number][i] * const + self.value[second_line_number][i]


    def elementary_transformation_1(self, first_line_number: int, second_line_number: int):
        # This function rearranges first line and second line

        first_line_number -= 1
        second_line_number -= 1

        self.value[second_line_number], self.value[first_line_number] = self.value[first_line_number], self.value[second_line_number]
    
    
    def transpose(self):
        # This function transpose the matrix

        temp = self.copy()
        
        for i in range(self.size):
            for j in range(self.size):
                self.value[i][j] = temp.value[j][i]


    def determinant(self) -> Z7_num:
        det = Z7_num(0)
        for start in range(self.size):
            mult = Z7_num(1)
            for i in range(self.size):
                mult *= self.value[i][(start + i) % self.size]
            det += mult
                # print(f"elem = {self.value[i][(start + i) % self.size]}")
                # print(f'det = {det}')
        # print("---------------------")
        for start in range(self.size):
            mult = Z7_num(1)
            for i in range(self.size):
                mult *= self.value[self.size - 1 - i][(start + i) % self.size]
            det -= mult
                # print(f"elem = {self.value[self.size - 1 - i][(start + i) % self.size]}")
                # print(f"det = {det}")
        return det



if __name__ == "__main__":
    A = Z7_Matrix(3, [1, 2, 3], [4, 5, 6], [7, 8, 9])
    A.elementary_transformation_1(1, 2)
    B = A.copy()
    B.transpose()
    print(B)
    print()
    print(A)
