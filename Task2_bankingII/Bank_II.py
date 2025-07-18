import random

#-----------------------------------

class Bank:

    banks = ['NBE', 'CIB', 'BANQUE MISR', 'QNB', 'NBK', 'AIB', 'ALEX BANK', 'BANQUE DU CAIRE', 'EGBANK', 'ARAB BANK', 'ADCB', 'AAIB']
    bank = random.choice(banks)

    def __init__(self,balance):
        self.balance = balance

    def checkBalance(self):
        return f" your current balance is {self.balance}"    

    def deposit(self,amountToAdd):
        self.balance += amountToAdd
        print(f"{amountToAdd} was successfully added to your balance")
        return self.balance
    
    def withdraw(self,amountToRemove):
        self.balance -= amountToRemove
        print(f"{amountToRemove} was successfully withdrawn from your balance")
        return self.balance
    
#---------------------------------------------------------------------------------------------------------

def ensureValidInput():
    while(True):
        userInput = input("kindly make ensure you input a positive digit value:  ")
        if userInput.isdigit() and int(userInput) > 0 : 
            userInput = int(userInput)
            break
        else: 
            print("invalid input")
            continue
    return userInput   


name = input("Enter Your Name: ") 

print("Enter Your Initial Balance")
balance = ensureValidInput()
banking = Bank(balance)

print(f"Welcome To {Bank.bank}")

while(True):
  
    choice = input("""would you like to
                   1. Check your balance
                   2. Deposit
                   3. withdraw
                   4. Exit
                   """)
    
    if not choice.isdigit():
       print("Please Enter a Valid Number From The Options")
       continue
    else: 
        choice = int(choice)
    
    match choice:

       case 1:
          print(banking.checkBalance())

       case 2:
          print("Enter The Amount To Deposit: ")
          depositAmount = ensureValidInput()
          banking.deposit(depositAmount)

       case 3:
           print("please enter the amount withdraw: ")
           withdrawAmount = ensureValidInput()
           if (withdrawAmount <= banking.balance):    
               banking.withdraw(withdrawAmount)
           else:   
               print("Sorry! Can not Perform This Operation (Not Enough Fund)")

       case 4:
            print(f"Thank You for Choosing {Bank.bank}, See You Soon!")
            break

       case _:
            print("Sorry Couldn't Understand Your Choice Please Try Again Later")
    

    print(f"your current balance is {banking.balance}")

    choice2 = input("Do you Want to continue ? 1/Yes   ")
    if choice2.isdigit() and int(choice2) == 1: continue
    else: 
        print(f"Thank You for choosing {Bank.bank}, See you soon!")
        break

#---------------------------------------------------------------------------------------------------
