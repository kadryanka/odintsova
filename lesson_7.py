# 1
class Matrrix:
    def __init__(self,li):
        self.li = li
    def __str__(self):
       return str("\n".join(["\t".join( [str(j)for j in i]) for i in self.li]))
    def __add__(self, other):
        for i in range(len(self.li)):
            for j in range(len(other.li[i])):
                self.li[i][j] = self.li[i][j] + other.li[i][j]
        return Matrrix.__str__(self)


m_1 = Matrrix([[31,22],[37,43],[51,86]])
m_2 = Matrrix([[3,5],[2,4],[-1,64]])

print (m_1.__add__(m_2))

#№ 2
from abc import ABC,abstractmethod
class Clothes(ABC) :

    @abstractmethod
    def consumption(selfl,p):
        pass

class Coat(Clothes):
    def __init__(self,size):
        self.size = size
    @property
    def s(self):
        return self.size
    @s.setter
    def s(self,size):
        self.size = size
    def consumption(self,size):
        if size > 70:
            return f"обратите внимание на размерную сетку"
        if size < 40:
            return f"обратите внимание на размерную сетку"
        else:
            consumption_on_coat = self.size //6.5 + 0.5
            return consumption_on_coat

class Jacket(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def h(self):
        return self.height

    @h.setter
    def h(self, height):
        self.height = height

    def consumption(self, height):
        if height > 300:
            return f"недопустимое значение"
        if height < 40:
            return f"недопустимое значение"
        else:
            consumption_on_jacket = 2 * self.height + 0.3
            return consumption_on_jacket
coat1 = Coat(56)
jacket1 =Jacket(170)

print(f"расход ткани на пальто в данном размере -  {coat1.consumption(56)} метров")
print(f"расход ткани на пиджак с данным параметром  {jacket1.consumption(170)} метров")




#№ 3
class Cell:
    def __init__(self,quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return f'количество ячеек в новой клeтке {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub < 0:
            return "проверьте данные"
        else:
            return f"в результате вычитания в новой клетке осталось {sub} ячеек"

    def __mul__(self, other):
        return f"количество ячеек в новой клетке в результате умножения {self.quantity*other.quantity}"
    def __truediv__(self, other):
        return f"в результате деления в новой клетке осталось {self.quantity//other.quantity} ячеек"
    def make_order(self,rez):
        res = ""
        for i in range(int(self.quantity/rez)):
            res += "*" * rez + "\n"
        res += "*" * (self.quantity % rez) + "\n"
        return res

cell = Cell (36)
cell_2 = Cell(6)
print(cell + cell_2)
print(cell - cell_2)
print(cell* cell_2)
print(cell / cell_2)
print(cell.make_order(6))



