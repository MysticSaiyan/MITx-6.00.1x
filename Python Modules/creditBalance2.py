from time import time
start = time()

balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = (0.2/12.0)
origBalance = balance

fixMonPay = 0
while balance > 0:
    fixMonPay += 10
    balance = origBalance
    for i in range(12):
        balance -= fixMonPay
        balance += (monthlyInterestRate*balance)

print("Lowest Payment: " + str(fixMonPay))

print(time() - start)

    
