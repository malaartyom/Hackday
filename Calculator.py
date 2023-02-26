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
    
    def __div__(self, other):
        if other == 0:
            raise ZeroDivisionError

        one = Z7_num(1)
        opposite_to_other = Z7_num(1)

        for i in range(1, 7):
            z7_i = Z7_num(i)
            if z7_i * other == one:
                opposite_to_other = Z7_num(i)
                break
                
        return self * opposite_to_other

    
    def __truediv__(self, other):
        return Z7_num.__div__(self, other)
    
    def __sub__(self, other):
        return Z7_num(self.value - other.value)
    
    def __neg__(self):
        return Z7_num(-self.value)
    
    def __int__(self):
        return self.value
    
    def __ge__(self, other):
        return self.value >= other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other) -> bool:
        if type(other) is int:
            return self.value == other
        return self.value == other.value


class Z7_Matrix:
    
    def __init__(self, num, *args):
        self.size = num
        self.value = [[Z7_num(0) for i in range(num)] for j in range(num)]
        
        if len(args) == 1:
            args = args[0]

        if args:
            for i in range(self.size):
                for j in range(self.size):
                    self.value[i][j] = Z7_num(args[i][j])
    

    def __str__(self) -> str:
        return_string = ""
        for i in range(self.size):
            for j in range(self.size):
                return_string += str(self.value[i][j])
                return_string += " "
            return_string += "\n"
        return return_string[:-1]

    def __mul__(self, other):
        return_matrix = Z7_Matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                summ = Z7_num(0)
                for k in range(self.size):
                    summ += self.value[i][k] * other.value[k][j]
                return_matrix.value[i][j] = summ
        return return_matrix

    def copy(self):
        # This function make deep copy of matrix
        copied = Z7_Matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                copied.value[i][j] = Z7_num(int(self.value[i][j]))

        return copied

    
    def sort_matrix(self):
        temp = self.copy()
        temp.value.sort(reverse=True)
        
        return_list = []
        
        for i in range(self.size):
            for j in range(i, self.size):
                if temp.value[i] == self.value[j]:
                    self.elementary_transformation_1(i + 1, j + 1)
                    return_list.append((1, (i + 1, j + 1)))
        return return_list


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
        # This function calculate determinant of the matrix
        
        det = Z7_num(0)

        for start in range(self.size):
            mult = Z7_num(1)
            for i in range(self.size):
                mult *= self.value[i][(start + i) % self.size]
            det += mult
        for start in range(self.size):
            mult = Z7_num(1)
            for i in range(self.size):
                mult *= self.value[self.size - 1 - i][(start + i) % self.size]
            det -= mult
        return det
    
    
    def superdiegonolise(self):
        return_list = []
        
        for index in range(self.size):
            j = self.size

            is_matching = True
            for i in range(index):
                    if self.value[0][i] != 0:
                        is_matching = False

            while (self.value[0][index] == 0 or not is_matching) and j > 1:
                self.elementary_transformation_1(1, j)
                return_list.append((1, (1, j)))
                is_matching = True
                for i in range(index):
                    if self.value[0][i] != 0:
                        is_matching = False
                        break
                j -= 1

            num = self.value[0][index]

            if num != 0:
                for i in range(1, self.size):
                    self.elementary_transformation_3(0 + 1, -(self.value[i][index] / num), i + 1)
                    return_list.append((3, (1, int(-(self.value[i][index] / num)), i + 1)))
                    
        return_list += self.sort_matrix()
        
        self.sort_matrix()

        return return_list


if __name__ == "__main__":
    A = Z7_Matrix(4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    b = A.superdiegonolise()
    print(A)
    print(b)

