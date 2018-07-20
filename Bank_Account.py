class Account:

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance


    def __str__(self):
        return "Your name is: %s \nYour account balance is: $%s\n" % (self.owner, self.balance)


    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print("Deposit Accepted")


    def withdrawl(self,withdraw):
        if (self.balance - withdraw) >= 0:
            self.balance = self.balance - withdraw
            print ("Withdrawl Accepted")
            print ("Available Funds: $%s" % (self.balance))
        else:
            print ("Funds Unavailable!")


#TEST THE CLASS ABOVE:

acct1 = Account('Jose',100)
print (acct1)

acct1.deposit(50)

print (acct1)

acct1.deposit(100)

print (acct1)

acct1.withdrawl(50)

print (acct1)

acct1.withdrawl(500)

print (acct1)

