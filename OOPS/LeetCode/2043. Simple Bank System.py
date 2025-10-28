class Bank:

    def __init__(self, balance: List[int]):
        # This is the balance of all n account stored in 0 index arr 
        self.balance = balance #[10, 100, 20, 50, 30]


    def transfer(self, account1: int, account2: int, money: int) -> bool:

        # lets check if both accounts exists 
        if not self.acc_exists(account1) or not self.acc_exists(account2):
            return False # invalid acc num 
        
        account1 = account1 - 1 # we are compensating the 0th index arr bank numbers 
        account2 = account2 - 1

        #[5, 1, 20] transfer amt from acc 5 -> acc 1 , 5 acc bala = 30-20= 10 and 1acc bala = 10+20 = 30 
        # lets have intial check to see if the transcation is valid 
        #check if acc 1 - money > 0 if yes then the transcation is possible and we can update the balances 

        if self.balance[account1] - money >= 0:
            # if the above cond is true then we need to update the balances
            self.balance[account1] -= money
            self.balance[account2] += money 
            return True
        else:
            return False #insufficient balance, transcation failed 

        

    def deposit(self, account: int, money: int) -> bool:



        # [5, 20] given acc num and money we need to deposit 
        if not self.acc_exists(account):
            return False # invalid acc number 
        
        account = account - 1 # to compensate 0 index arr 

        # if acc num exists we simple depost the money 
        self.balance[account] += money 
        return True # deposit sucessfull

        

    def withdraw(self, account: int, money: int) -> bool:


        #[3, 10] if acc 3 has given money then with draw is sucessful and the balance is updated 
        if not self.acc_exists(account):
            return False # invalid acc num 

        
        account = account - 1 # to compensate 0 index arr 
        
        # if the acc num exists then we have to check if the acc have enough money to withdraw 

        if self.balance[account] - money >= 0:
            # so if the acc has enough balance then we with draw the money 
            self.balance[account] -= money 
            return True # sucessfully withdrawn 
        else:
            return False # failed transcation due to insufficent balance

    #-------------------checker------------------------
    def acc_exists(self, account_num):
        return 1 <= account_num <= len(self.balance) # if the acc num is in this range then only proceed to valid transcation
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)