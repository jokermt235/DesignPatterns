from Notifier import Notifier
class StandartNotifier(Notifier):
    def send(self, message : str):
        print("Notifier says : " + message)
