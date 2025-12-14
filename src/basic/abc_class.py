from abc import ABC, abstractmethod

from typing_extensions import override


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def get_fee(self):
        return 0.5

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

    @override
    def get_fee(self):
        return 1.0