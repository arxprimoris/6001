balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minMonthly = 0.0
totalPaid = 0.0
for month in range(0, 12):
	minMonthly = balance * monthlyPaymentRate
	newBalance = balance - minMonthly
	balance = newBalance + (newBalance * (annualInterestRate/12.0))
	print("Month: " + str(month+1))
	print("Minimum monthly payment: " + str(round(minMonthly,2)))
	print("Remaining balance: " + str(round(balance,2)))
	totalPaid += minMonthly
	

print("Total paid: " + str(round(totalPaid,2)))
print("Remaining balance: " + str(round(balance,2)))