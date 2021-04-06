from GasEngine import GasEngine
class Car:
    engine = None
    def __init__(self, engine : GasEngine):
        self.engine = engine