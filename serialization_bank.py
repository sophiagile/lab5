import json 

class Customer: 
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name 

    def to_json(self): 
        return json.dumps({
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }, indent=2)
    
john = Customer(1, "John", "Smith")

print(john.to_json())

class Account:
    def __init__(self, account_id,balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        return json.dumps({
            "account_id": self.account_id,
            "balance": self.balance
        }, indent=2)
    
john_account = Account(1,5000)

print(john_account.to_json())