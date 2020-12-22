import os

def traverse(dir):
	print(dir)
	tempcwd = os.getcwd()
	if os.path.isdir(os.path.join(tempcwd, dir)):
		for d in os.listdir(os.path.join(tempcwd, dir)):
			os.chdir(os.path.join(tempcwd, dir))
			traverse(d)
			os.chdir(tempcwd)

traverse(".")