from time import sleep as s

print("\n" * 25)
commands = ["cd", "cd..", "echo", "ls", "type"]
directory = ["C:\\"]
directoryFiles = {}



def debug(input):
	print("[DEBUG] %s" % input)



while 1:
	try:
		main = input("%s>" % (directory[0] + "\\".join(directory[1:])))
	except:
		main = input(">")



	mainSplit = main.split(" ")
	mainEchoSplit = main.split(" > ")



	if not mainSplit[0] in commands:
		print("'%s' is not recognized as an internal or external command,\noperable program, or batch file." % main)

	elif mainSplit[0] == "cd":
		if len(directory) == 0:
			mainSplit[-1] += "\\"
		directory.append("%s" % " ".join(mainSplit[1:]))

	elif mainSplit[0] == "cd..":
		del directory[-1]

	elif mainSplit[0] == "echo":
		mainEchoSplit[0] = mainEchoSplit[0][5:]
		fileDict = {mainEchoSplit[1]: mainEchoSplit[0]}
		if directory[-1] in directoryFiles:
			directoryFiles[directory[-1]][mainEchoSplit[1]] = mainEchoSplit[0]
		else:
			directoryFiles[directory[-1]] = {mainEchoSplit[1]: mainEchoSplit[0]}

	elif mainSplit[0] == "ls":
		if not (directory[-1] in directoryFiles):
			print("The current directory does not have any files.")
		else:
			for file in directoryFiles[directory[-1]]:
				print(file)

	elif mainSplit[0] == "type":
		if not (directory[-1] in directoryFiles):
			print("The current directory does not have any files.")
		else:
			if not (" ".join(mainSplit[1:]) in directoryFiles[directory[-1]]):
				print("That file does not exist in the current directory.")
			else:
				print(directoryFiles[directory[-1]][" ".join(mainSplit[1:])])



	print()