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
