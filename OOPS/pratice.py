class Atm:

    def __init__(self,pin=None,balance=0):
        self.pin = pin
        self.balance = balance
        self.menu()

    def menu(self):
        user_input = input(
            """
            press 1: To create pin
            press 2: To update pin
            press 3: To check balance
            press 4: To with draw
            """
        )
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.update_pin()
        elif user_input == '3':
            self.check_balance()
        else:
            amount = int(input('Enter the amount'))
            self.withdraw(amount)

    def create_pin(self):
        user_input = input("Enter new_pin..")
        self.pin = user_input

        user_balance = int(input("Enter balance"))
        self.balance = user_balance

        

    def update_pin(self):
        if self.pin is None:
            print('create new pin')
            return 
        
        user_input = input("enter old pin")
        if user_input != self.pin:
            print('incorrect old pin')
            return 

        user_new_pin = input('enter new pin')
        self.pin = user_new_pin

    def check_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return 'insufficent funds'
        self.balance -= amount
        return 'amount sucessfully withdrawn'
    
        
obj = Atm()
print(obj.pin)
print(obj.balance)
obj.update_pin()
print(obj.pin)
