import random
import matplotlib.pyplot as plt
account=int(input("Enter the amount in your account reserved for lottery: "))
initial_account=account
bet_amount=int(input("Enter the bet amount for lottery: "))

#if one wins, he will get nine fold of the bet amount or loses the bet amount

x=[]
y=[]
for i in range(366):
    if account<=0 and i<366:
        print("you got banrupted after",i,"times of bet. better luck next time")
        break
    else:
        bet_ticket=random.randint(1,10)
        lottery_ticket=random.randint(1,10)
        x.append(i+1)
        if bet_ticket==lottery_ticket:
            account=account + (bet_amount*9)
        else:
            account=account-bet_amount
        y.append(account)
plt.plot(x,y)
plt.show()
if account>=initial_account:
    profit=account-initial_account
    print("Finally after",i," number of bets, the amount in the account is",account,"after a profit of",profit)
else:
    loss=initial_account-account
    print("Finally after",i," number of bets, the amount in the account is",account,"incurring a loss of",loss)
