import os
from os import listdir
from os.path import isfile, join

to_delete = ['.exe', '.bat']
to_move = ['.zip']

def extensionIn(file_name, extension_list):

	for extension in extension_list:
		if extension in file_name:
			return True

	return False

def main():

	dir = os.path.dirname(os.path.realpath(__file__))
	files = [f for f in listdir(dir) if isfile(join(dir, f))]

	if not os.path.isdir(dir + '/zip'):
		os.makedirs(dir + '/zip')

	for file_name in files:
		if extensionIn(file_name, to_delete):
			os.remove(file_name)
			print('deleting ' + file_name + '...')
		elif shouldMove(file_name, to_move):
			os.rename(file_name, dir + '/zip/' + file_name)
			print('moving ' + file_name + '...')

	print('done!')

if __name__ == '__main__':
	main()