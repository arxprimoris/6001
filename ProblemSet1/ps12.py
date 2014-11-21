s = "azcbobobegghakl"
bobCount = 0
index = 0

while index < len(s):
	print(s[index:index+3])
	if s[index:index+3] == "bob":
		bobCount += 1
	index += 1

print("Number of times bob occurs is: " + str(bobCount))
