from  ITransportFactory import ITransportFactory
from Transport import Transport
from Car import Car
class CarFactory(Transport,ITransportFactory):
    def create() -> Car:
        return Car("Toyota")
