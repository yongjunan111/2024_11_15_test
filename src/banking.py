from abc import ABC, abstractmethod


class InterestStrategy(ABC):
    @abstractmethod
    def apply_interest(self, money):
        pass


class Member(InterestStrategy):
    def apply_interest(self, money):
        print('No Discount')

        return money