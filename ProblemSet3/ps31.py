def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def leftRiemann(function, left, right, delta):
	step = float(left)
	value = 0
	while step < right:
		value += (function(step)*delta)
		step += delta
	return value

def main():
	start = 40
	stop = 100
	step = 1.5

	print(str(leftRiemann(f, start, stop, step)))

main()
