def run():
	import numpy
	numpyLst = dir(numpy)
	numpyFns = open('numpyFunctions.txt','w+')
	for line in range(len(numpyLst)):
		numpyFns.write(numpyLst[line])
		numpyFns.write('\n')
	numpyFns.close()

run()