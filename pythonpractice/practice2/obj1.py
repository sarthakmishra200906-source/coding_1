class car ():
    carname="BMW"
    carmodel="X5"
    caryear=2020
    def __init__(self,carcolour,carprice):
       self.carcolour=carcolour
       self.carprice=carprice

car1=car("Black",1000000)
print(car1.carname)
print(car1.carcolour)
print(car1.carprice)
