
balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = (annualInterestRate/12.0)
origBalance = balance
lo = balance/12.0
hi = (balance*(1+monthlyInterestRate)**12)/12.0

while True:
    balance = origBalance
    fixMonPay = (hi+lo)/2
    for i in range(12):
        balance -= fixMonPay
        balance += (monthlyInterestRate*balance)
    if balance > 0.01:
        lo = fixMonPay
    elif balance < -0.01:
        hi = fixMonPay
    else:
        break

print("Lowest Payment: " + str(round(fixMonPay,2)))
