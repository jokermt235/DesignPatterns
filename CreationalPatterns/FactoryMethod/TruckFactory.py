from  ITransportFactory import ITransportFactory
from Transport import Transport
from Truck import Truck
class TruckFactory(Transport,ITransportFactory):
    def create() -> Truck:
        return Truck("Howo")