def derivatives(f, x, h=0.0001):
	df = (f(x+h) - f(x-h)) / (2 * h)
	ddf = (f(x+h) - 2*f(x) + f(x-h)) / h**2
	return df, ddf

def run():
	from math import sin, pi
	dsin, ddsin = derivatives(sin, pi/4)
	print('first derivative = {:6.4F}'.format(dsin))
	print('second derivative = {:6.4F}'.format(ddsin))

run()