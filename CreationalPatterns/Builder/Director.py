from CarBuilder import CarBuilder
from models.Transmission import Transmission
from models.Engine import Engine
class Director:
    def constructCar(self, builder : CarBuilder):
        builder.reset()
        builder.setWheelCount(4)
        builder.setTransmission(Transmission('automatic'))
        builder.setEngine(Engine(2.2))
