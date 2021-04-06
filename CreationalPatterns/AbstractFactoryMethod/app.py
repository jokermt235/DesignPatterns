from TransportFactory import TransportFactory
from CarFactory import CarFactory
from TruckFactory import TruckFactory

factory = TransportFactory()
car = factory.createTransport(CarFactory)
truck = factory.createTransport(TruckFactory)
#Base class not touched
print(car.getName())
print(truck.getName())
