# № 1
class Data:
    data = ""
    def __init__(self, data):
        self.data = data

    @classmethod
    def set_data(cls,str):
        li = str.split("-")
        print("day:",li[0])
        print("month:",li[1])
        print("year:",li[2])
        return [int(el) for el in li]

    @staticmethod
    def valid(day,month,year):
        if 1 <= day >= 31:
            print("day error")
        elif 1 <= month >= 12:
            print('month error')
        elif 2022 >= year <= 0:
            print("year error")


data = Data("04-13-1976")
li = Data.set_data(data.data)
Data.valid(li[0],li[1],li[2])


# # # 2
class WorkTime:
    def __init__(self,count_day,count_our):
        self.count_day = count_day
        self.count_our = count_our
    @staticmethod
    def one_day(count_day,count_our):
        try:
            return (count_day/count_our)
        except:
            return (f"делить на ноль нельзя")
time = WorkTime(200,20)
print(time.one_day(200,20))
print(time.one_day(20,260))
print(WorkTime.one_day(34,0))

# # 3
class Number(Exception):
    def __init__(self,li):
        self.li = li
    def __str__(self):
        return self.li
if __name__ == '__main__':
    my_li = []
    while True:
        user_input = input("введите данные или стоп для выхода:" )
        if user_input == "стоп":
            break
        try:
                if not user_input.isdigit():
                    raise Number(f"'{user_input}'ошибка!! вводится только число")
                my_li.append(int(user_input))
        except Number as el:
                print(el)
        print(my_li)

 # 4
class StoreMashines:
     def __init__(self,name,price,quantity):
         self.name = name
         self.prise = price
         self.quantity = quantity
         self.item =  {'модель ': self.name,'цена за шт.': self.prise,'количество': self.quantity}
     def income(self):

             try:
                name= input(f"введите назавание:")
                price = int(input(f'введите цену за 1 шт.:'))
                quantity = int(input(f'введите количество:'))
                item = {'модель устройства': name,'цена за 1 шт.': price,'количество':quantity}
                self.item.update(item)
                print(self.item)

             except ValueError:
                 print( f'ошибка ввода')

class Printer(StoreMashines):
    pass
class Scanner(StoreMashines):
    pass
p = Printer ('epcon',5,23400)
s = Scanner ('epson',2,56000)
p.income()
s.income()















