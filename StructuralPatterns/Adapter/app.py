from EngineAdapter import EngineAdapter
from GasEngine import GasEngine
from ElectroEngine import ElectroEngine
from Car import Car

car = Car(GasEngine(250))
car2 = Car(ElectroEngine(100))