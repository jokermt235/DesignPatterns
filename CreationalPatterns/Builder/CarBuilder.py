from models.ICar import ICar
from models.Car import Car
from models.Transmission import Transmission
from models.Engine import Engine
class CarBuilder(ICar):
    def reset(self):
        self.car = Car()
    def setWheelCount(self,count : int):
        self.car.wheels = count
    def setTransmission(self , transmission : Transmission ):
        self.car.transmission = transmission
    def setEngine(self, engine : Engine):
        self.car.engine = engine
    def getResult(self) -> Car :
        return self.car