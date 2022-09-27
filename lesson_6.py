#№ 1
from time import sleep
class TrafficLight:
    __color = "yellow"
    print("сейчас горит красный")
    sleep(7)
    print("сейчас загорелся желтый")
    sleep(2)
    print('загорелся зеленый')
    sleep(5)

# № 2
class Road:
    def __init__(self,lenght,width):
        self._lenght = lenght
        self._width = width
    def formula(self):
        return f"масса асфальта равна :{(self._lenght * self._width * 25 * 0.05) / 1000}"
my_road = Road(50,4)
print(my_road.formula())

# № 3
class Woker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        #self._income = income
        self._income = {"wage":wage,"bonus":bonus}
class Position(Woker):
    def get_full_name(self):
        return f"{self.name} {self.surname} {self.position}"
    def get_total_income(self):
        return f"{sum(self._income.values())}"
my_position = Position("Andrey","Petrov","doctor",230,34)
print(my_position.get_full_name())
print(my_position.get_total_income())
# № 4
class Car:
    def __init__(self,speed,color,name,is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'автомобиль марки {self.name}, цвет {self.color},полиция?{self.is_police}')

    def stop(self):
        return f'{self.name:} остановилася'
    def go(self):
        return f'{self.name:} поехал'
    def turn(self,direction):
        print(f'автомобиль {self.name} повернул {"налево" if direction == 0 else "направо"}')
    def show_speed(self):
        print( f'автомобиль{self.name} едет со скоростью {self.speed}')

class TownCar(Car):
     def show_speed(self):
        print( f'автомобиль{self.name} едет со скоростью {self.speed}{"снизьте скорость!!" if self.speed > 80 else "вы аккуратный водитель"}')


class WorkCar(Car):
    def show_speed(self):
         print( f'автомобиль {self.name} едет со скоростью {self.speed} {"снизьте скорость!!" if self.speed > 90 else "вы аккуратный водитель"}')

class SportCar(Car):
     pass
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(name,color,speed,is_police)
    W_Car = WorkCar(150, "белый","scoda")
    print(W_Car)
    print(W_Car.show_speed())

# № 5
class Stetionery:
    def __init__(self,title):
        self.titly = title
    def draw(self):
        print(f"запуск отрисовки{self.titly}")
class Pen(Stetionery):
    def draw(self):
        print(f"отрисовка начата ручкой {self.titly}")


class Pencil(Stetionery):
    def draw(self):
        print(f"начало отрисовки карандашом {self.titly}")
class Handly(Stetionery):
    def draw(self):
        print(f" отрисовка начата маркером {self.titly}")


my_pencil = Pencil("какого-то китайского производства")
print(my_pencil.draw())




