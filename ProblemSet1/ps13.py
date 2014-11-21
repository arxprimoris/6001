s = "alkdjfpoiqjewlnablkafyqeroithapoieqjdslknvkajhdfgkjahdgiuayabcdefghirtkjanvlkjanflkjghaoi"

leftIndex = 0
rightIndex = 1
longest = ""

while leftIndex < len(s):
	while rightIndex < len(s) and s[rightIndex-1] <= s[rightIndex]:
		rightIndex += 1
	if len(longest) < rightIndex - leftIndex:
		longest = s[leftIndex:rightIndex]
	leftIndex = rightIndex
	rightIndex += 1

print("Longest substring in alphabetical order is: " + longest)
