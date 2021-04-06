from CarFactory import CarFactory
from TruckFactory import TruckFactory

car = CarFactory.create()
truck = TruckFactory.create()
#Base class not touched
print(car.getName())
print(truck.getName())
