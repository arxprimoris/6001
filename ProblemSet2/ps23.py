balance = 999999
annualInterestRate = 0.18
numPeriods = 12

def checkPayment(paymentValue):
	newBalance = balance
	for month in range(0, numPeriods):
		newBalance = newBalance - paymentValue
		newBalance	 = newBalance + (newBalance * (annualInterestRate/float(numPeriods)))
		# print("Month: " + str(month+1))
		# print("Remaining balance: " + str(round(newBalance,2)))

	return(newBalance)

endingBalance = balance
upperBound = (balance * (1 + float(annualInterestRate/numPeriods))**numPeriods)/float(numPeriods)
lowerBound = balance / float(numPeriods)

while((upperBound - lowerBound) >= 0.0001):
	payment = (lowerBound + upperBound)/2.0
	endingBalance = checkPayment(payment)
	if(endingBalance < 0):
		upperBound = payment
	elif(endingBalance > 0):
		lowerBound = payment
	# print(payment)
	# print(endingBalance)

print("Lowest payment: " + str(round(payment,2)))
print("Ending balance: " + str(endingBalance))