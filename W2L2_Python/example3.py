def run():
	import numpy as np
	import matplotlib.pyplot as plt
	x = np.arange(0.0, 2*np.pi, np.pi/25)
	plt.plot(x, np.sin(x), 'o-r', x, np.cos(x), '^-b')
	plt.xlabel('x')
	plt.ylabel('values')
	plt.title('Trigonometric Functions')
	plt.legend(('sine', 'cosine'), loc=3)
	plt.savefig('trigPlot.png', format='png')
	plt.show()
	
run()