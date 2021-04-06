from  Director import Director
from CarBuilder import CarBuilder

director = Director()

carBuilder = CarBuilder()

director.constructCar(carBuilder)

car = carBuilder.getResult()

print(car.getWheelCount())