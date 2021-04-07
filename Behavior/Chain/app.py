from StandartNotifier import StandartNotifier
from EmailNotifier import EmailNotifier
notifier = StandartNotifier()
notifier2 = EmailNotifier()

notifier.send("Hello this is not so important")

notifier.setNextNotifier(notifier2)

notifier.send("Hello this is slightely important")