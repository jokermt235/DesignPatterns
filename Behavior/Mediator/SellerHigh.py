from Seller import Seller
class SellerHigh(Seller):
    product = None
    def __init__(self, product: Product):
        self.product = product
    def sell(self, seller : Seller):
