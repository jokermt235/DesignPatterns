from Notifier import Notifier
class EmailNotifier(Notifier):
    def send(self, message : str):
        print("Notifier email says : " + message)
