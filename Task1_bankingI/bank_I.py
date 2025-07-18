
import random

#--------------------------------------------------------------------

def checkBalance(balance):
    return f" your current balance is {balance}"

def deposit(balance,x):
    newBalance= balance + x
    print(f"{x} was successfully added to your balance")
    return newBalance

def withdraw(balance,y):
    newBalance = balance - y
    print(f"{y} was successfully withdrawn from your balance")
    return newBalance

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

#---------------------------------------------------------------------

banks = ['NBE', 'CIB', 'BANQUE MISR', 'QNB', 'NBK', 'AIB', 'ALEX BANK', 'BANQUE DU CAIRE', 'EGBANK', 'ARAB BANK', 'ADCB', 'AAIB']
bank = random.choice(banks)
print(f"welcome to {bank}")



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
          print(checkBalance(balance))

       case 2:
          print("Enter The Amount To Deposit: ")
          depositAmount = ensureValidInput()
          balance= deposit(balance,depositAmount)

       case 3:
           print("please enter the amount withdraw: ")
           withdrawAmount = ensureValidInput()
           if (withdrawAmount <= balance):    
               balance= withdraw(balance,withdrawAmount)
           else:   
               print("Sorry! Can not Perform This Operation (Not Enough Fund)")

       case 4:
            print(f"Thank You for Choosing {bank}, See You Soon!")
            break

       case _:
            print("Sorry Couldn't Understand Your Choice Please Try Again Later")
    

    print(f"your current balance is {balance}")

    choice2 = input("Do you Want to continue ? 1/Yes   ")
    if choice2.isdigit() and int(choice2) == 1: continue
    else: 
        print(f"Thank You for choosing {bank}, See you soon!")
        break

#---------------------------------------------------------------------------------------------------