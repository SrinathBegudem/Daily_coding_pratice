# # class vs Object
# class Student:
#     def __init__(self,name,s1,s2,s3):
#         self.name = name
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
    
#     def get_avg(self):
#         return (self.s1+self.s2+self.s3)/ 3

# obj = Student('srinath',90,95,100)
# print(obj.get_avg())

class Account:
    def __init__(self,account_no,balance):
        if balance < 0:
            raise ValueError('intial balance cannot be negative')
        self.__account_no = account_no
        self.__balance = balance
    
    def credit(self,amount):
        if not isinstance(amount,(float,int)):
            raise ValueError('invalid data type, enter int or float.')
        if amount <= 0:
            raise ValueError('credit cannot be negative and must be greater than 0.')
        
        self.__balance += amount
        print('sucessfully credited....')

    def debit(self,amount):
        if not isinstance(amount,(float,int)):
            raise ValueError('invalid data type, enter int or float.')
        if amount <= 0:
            raise ValueError('credit cannot be negative and must be greater than 0.')

        if amount > self.__balance:
            raise ValueError(f'insufficent balance,your total balance is {self.__balance}')

        self.__balance -= amount
        print('amount sucesfully debitted..')
    
    def get_balance(self):
        return self.__balance

obj1 = Account(1234,1000)
print(obj1.get_balance())
obj1.credit(500)
print(obj1.get_balance())
# obj1.credit(-500)
obj1.debit(1000)
print(obj1.get_balance())

