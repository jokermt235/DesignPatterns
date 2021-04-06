class Logger:
    instance = None
    @staticmethod
    def getInstance() :
        if Logger.instance is None:
            Logger.instance = Logger()
        return Logger.instance

    def log(self, message : str):
        print(message)
