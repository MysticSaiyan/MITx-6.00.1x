balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    payment = balance * monthlyPaymentRate
    balance -= payment
    balance += ((annualInterestRate/12.0)*balance)

print("Remaining balance: " + str(round(balance,2)))