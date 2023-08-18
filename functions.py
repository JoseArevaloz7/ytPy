class Payment:
    initial_balance = 1000
    
    def __init__(self, recipient, amount):
        self.recipient = recipient
        self.amount = amount
    def check_balance(self):
        return Payment.initial_balance - self.amount
    
    @classmethod
    def update_initial_balance(cls, new_balance):
        cls.initial_balance = new_balance
    
    @staticmethod
    def check_valid_transaction(hour):
        if hour >= 8 and hour <= 17:
            return True
        return False
    

payment1 = Payment('A', 25) 
Payment.update_initial_balance(32)
print(payment1.initial_balance)