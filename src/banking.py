from abc import ABC, abstractmethod


class InterestStrategy(ABC):
    @abstractmethod
    def apply_interest(self, money):
        pass


class Member(InterestStrategy):
    def apply_interest(self, money):
        print('No Discount')

        return money
    

class PremiumMember(InterestStrategy):
    def apply_interest(self, money):
        interest = money * 0.0024
        print(f'PremiumMember interest: {interest}')

        return money + interest