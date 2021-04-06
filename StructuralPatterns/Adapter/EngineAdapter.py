from GasEngine import GasEngine
from ElectroEngine import ElectroEngine
class EngineAdapter(ElectroEngine, GasEngine):
    def getPower() -> float :
        return (self.getPowerHp() + self.getPowerWatt()) / 2 
        
