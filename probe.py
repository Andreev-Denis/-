class Car():
    def price(self):
        self.price = 1000000

    def horse_power(self):
        self.horse_power = 250

    def __str__(self):
        return ' Стоимость:{} Лошадиных сил:{}'.format(self.price, self.horse_power)

class Nissan(Car):
    def price(self):
        self.price = 150000

    def horse_power(self):
        self.horse_power = 150


class Kia(Car):
    def price(self):
        self.price = 100000


    def horse_power(self):
       self.horse_power = 100

car = Car()
car.price()
car.horse_power()
print(car)

Nissan = Nissan()
Nissan.price()
Nissan.horse_power()
print(Nissan)

Kia = Kia()
Kia.price()
Kia.horse_power()
print(Kia)
