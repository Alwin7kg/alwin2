class Bank:
    def __init__(self,accNo,name,typ,bal):
        self.acc=accNo
        self.n=name
        self.t=typ
        self.b=bal
    def deposit(self,amt1):
        self.b+=amt1
        printf("Balance: ",self.b)
    def withdraw(self,amt2):
        if self.b<amt2:
            print("Insufficient Balance")
        else:
            self.b-=amt2
            print("Balance: ",self.b)
    def display(self):
        print('\nAccno:',self.acc,'\nAccount holder name:',self.n,'\nAcc Type:',self.t,'\nBalance:',self.b)
        print("**MENU**")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Display")
        print("4.Exit")
        b1=Bank(1002,"Nidhi","Savings",0)
        b1.display()
        while True:
            choice=int(input("\nEnter your choice(1-4): "))
            if choice==1:
                d=int(input("Enter amount to be deposited: "))
                b1.deposit(d)
            elif choice==2:
                w=int(input("Enter amount to withdraw: "))
                b1.withdraw(w)
            elif choice==3:
                b1.display()
            elif choice>4:
                print("Enter a valid choice")
            else:
                break;
        
