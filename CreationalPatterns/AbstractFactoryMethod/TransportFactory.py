from Transport import Transport
from ITransportFactory import ITransportFactory
class TransportFactory:
    def createTransport(self, transportFactory: ITransportFactory) -> Transport:
        return transportFactory.create()
