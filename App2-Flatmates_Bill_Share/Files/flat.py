class Bill:
    """
    Creates a class Bill like electricity bill which has amount and the period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a class Flatmate with attributes name and number of days stayed.
    It also a method to calculate the share in the bill
    """

    def __init__(self, name, days_stayed):
        self.name = name
        self.days_stayed = days_stayed

    def pays(self, bill, flatmate2):
        weight = self.days_stayed / (self.days_stayed + flatmate2.days_stayed)
        to_pay = weight * bill.amount
        return to_pay
