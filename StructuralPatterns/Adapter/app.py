from EngineAdapter import EngineAdapter
from GasEngine import GasEngine
from ElectroEngine import ElectroEngine
from Car import Car

engineAdapter = EngineAdapter()
car = Car(EngineAdapter())
print(car.engine.getPower())
