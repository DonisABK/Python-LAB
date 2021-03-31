class BankAccount:
    def __init__(self,acc,no,t,b):
        self.acno=acc
        self.name=no
        self.type=t
        self.bal=b
    def deposit(self,acc):
        self.bal+=acc
        print('Rs.',acc,'deposited! Current balance is: Rs.',self.bal)
    def withdraw(self,acc):
        if self.bal >= acc:
            self.bal-=acc
            print('Rs.',acc,'withdrawn! Current balance is: Rs.', self.bal)
        else:
            print('Insufficient balance to make this transaction!')
acc=int(input('Enter account number:'))
no=input('Enter name of the account holder: ')
t=input('Enter account type: ')
b=float(input('Enter your balance:'))
ac1=BankAccount(acc,no,t,b)
ac1.deposit(float(input('Enter amount to deposit: ')))
ac1.withdraw(float(input('Enter amount to withdraw: ')))