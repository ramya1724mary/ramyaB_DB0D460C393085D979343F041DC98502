class BankAccount:
   def __init__(self,  account_number, account_holder_name, initial_balance=0.0):
       self.__account_number= account_number
       self.__account_holder_name= account_holder_name
       self.__account_balance= initial_balance

   def deposit(self,amount):
     if amount > 0:
       #self.__account_balance += amount
       print("deposited ₹{}. New balance: ₹{}".format(amount,
          self.__account_balance))
     else:
        print("invalid deposit amount. please deposit positive amount")

   def withdraw(self,amount):
       if amount > 0 and amount <= self.__account_balance:
        self.__account_balance -= amount         
        print ("Withdrawl ₹{}. New balance ₹{}". format(amount, self. __account_balance))
       else:
        print("invalid withdrawl account or insufficient balance.")

   def display_balance(self):
     print("Account balance {} (Account #{}): ₹{}".format(    self.__account_holder_name, self. __account_number, self.__account_balance))

#create an instance of the BankAccount class
Account=BankAccount(account_number="1234567890", account_holder_name="Jessy", initial_balance="5000.0") 

#test the deposit and withdrawal functionality. 
Account.display_balance()
Account.deposit(500.0)