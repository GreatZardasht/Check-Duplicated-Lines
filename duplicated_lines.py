import sys

class ColorPrint:
    @staticmethod
    def print_fail(message, end = '\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)
    @staticmethod
    def print_success(message, end = '\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)
    @staticmethod
    def print_warn(message, end = '\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)
    @staticmethod
    def print_info(message, end = '\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)
    @staticmethod
    def print_bold(message, end = '\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)

def main():	
	try:
		print('\x1b[1;34m' + '			   Duplicated lines checker' + '\x1b[0m')
		print('\x1b[1;33m' + '		      __...--~~~~~-._   _.-~~~~~--...__' + '\x1b[0m')
		print('\x1b[1;33m' + '		    //                 |               \\\\' + '\x1b[0m')
		print('\x1b[1;33m' + '		   //                 |                 \\\\' + '\x1b[0m')
		print('\x1b[1;33m' + '		  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\\' + '\x1b[0m')
		print('\x1b[1;33m' + '		 //__.....----~~~~._\\ | /_.~~~~----.....__\\\\' + '\x1b[0m')
		print('\x1b[1;33m' + '		====================\\\|//====================' + '\x1b[0m')
		print('\x1b[1;33m' + '		                    `---`' + '\x1b[0m')
		print('\x1b[1;33m' + '               Coded by Krypton - https://github.com/kkrypt0nn' + '\x1b[0m')
		print('')
		print('')
		ColorPrint.print_bold("Please give the file name: ")
		file = input('> ')
		if ".txt" not in file:
			file = file + ".txt"
		else:
			pass
		ColorPrint.print_bold('Do you want to create a new file with the duplicated lines removed after the scan?')
		remove = input('> ')
		if remove.lower() == 'yes' or remove.lower() == 'y' or remove.lower() == 'ye':
			ColorPrint.print_bold('What should be the new file name ?')
			new_file = input('> ')
			if ".txt" not in new_file:
				new_file = new_file + ".txt"
			else:
				pass
			outfile = open(new_file, "w")
			lines_seen = set()
			ColorPrint.print_bold('------------------------------')
			ColorPrint.print_info('Duplicated lines:')
			with open(file) as f:
				seen = set()
				for line in f:
					if line in seen:
						print(line)
					else:
						seen.add(line)
			ColorPrint.print_bold('------------------------------')
			for line in open(file, "r"):
				if line not in lines_seen:
					outfile.write(line)
					lines_seen.add(line)
			outfile.close()
			ColorPrint.print_success('File created under the name "' + new_file + '".')
		else:
			ColorPrint.print_bold('------------------------------')
			ColorPrint.print_info('Duplicated lines:')
			with open(file) as f:
				seen = set()
				for line in f:
					if line in seen:
						print(line)
					else:
						seen.add(line)
			ColorPrint.print_bold('------------------------------')

	except FileNotFoundError:
		ColorPrint.print_fail('Could not find duplicated lines. File not found.')
	except KeyboardInterrupt:
		ColorPrint.print_fail('\nYou pressed CTRL+C, so the programm stopped.')

main()