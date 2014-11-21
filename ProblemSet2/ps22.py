balance = 3926
annualInterestRate = 0.2
numPeriods = 12

def checkPayment(paymentValue):
	newBalance = balance
	for month in range(0, numPeriods):
		newBalance = newBalance - paymentValue
		newBalance	 = newBalance + (newBalance * (annualInterestRate/float(numPeriods)))
		# print("Month: " + str(month+1))
		# print("Remaining balance: " + str(round(newBalance,2)))

	return(newBalance)

payment = 10
endingBalance = 0
while(True):
	endingBalance = checkPayment(payment)
	if(endingBalance <= 0):
		break
	payment += 10

print("Lowest payment: " + str(payment))
print("Ending balance: " + str(endingBalance))