from DatabaseEngine from DatabaseEngine
class Database:
    engine = None
    def __init__(self, engine : DatabaseEngine ):
        self.engine = engine
