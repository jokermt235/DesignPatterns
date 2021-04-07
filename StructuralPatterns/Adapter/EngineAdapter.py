from GasEngine import GasEngine
from ElectroEngine import ElectroEngine
class EngineAdapter(ElectroEngine, GasEngine):
    def getPower(self) -> str :
        return str(self.getPowerHp()) + "hp" + "," + str(self.getPowerWatt()) + "watt"
        
