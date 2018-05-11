import os
from os import listdir
from os.path import isfile, join

toDelete = ['.exe', '.bat']
toMove = ['.zip']

def shouldDelete(file_name):

	for extension in toDelete:
		if extension in file_name:
			return True

	return False

def shouldMove(file_name):

	for extension in toMove:
		if extension in file_name:
			return True
	
	return False

def main():

	dir = os.path.dirname(os.path.realpath(__file__))
	files = [f for f in listdir(dir) if isfile(join(dir, f))]

	if not os.path.isdir(dir + '/zip'):
		os.makedirs(dir + '/zip')

	for file_name in files:
		if shouldDelete(file_name):
			os.remove(file_name)
			print('deleting ' + file_name + '...')
		elif shouldMove(file_name):
			os.rename(file_name, dir + '/zip/' + file_name)
			print('moving ' + file_name + '...')

	print('done!')

if __name__ == '__main__':
	main()