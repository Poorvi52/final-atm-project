class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("Rupees = 5000")
        print("Paise = 50")

    def withdrawl1(self,rupees):
        new_amount = 5000 - rupees
        print("You have withdrawn amount "+str(rupees) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,paise):
        new_amount = 50 - paise
        print("You have withdrawn amount "+str(paise) + ". Your remaining balance is "+ str(new_amount))

def main():
    print("Welcome to Poorvi's Bank!")
    Account = input("Enter your card number and pin number:")
    card_number = input("Enter your card number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add Rupees")
        print("2. Add Paise")
        choose = int(input("1. Add Rupees  2. Add Paise"))
        if (choose == 1):
           rupees = int(input("Enter the amount:- "))
           new_user.withdrawl1(rupees)
        if (choose == 2):
           paise = int(input("Enter the amount:- "))
           new_user.withdrawl2(paise)    
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()