from random import randint as ri
from time import sleep as s
from timeit import default_timer as timer
import os

clear = lambda: os.system('cls')

while 1:
	alreadyChosen = []
	done = False
	total = 0

	inputCombo = input("What is your locker combination?\n")
	clear()

	startOf = timer()

	while not done:
		# clear()
		combo = "-".join(["%s" % ri(0,45), "%s" % ri(0,45), "%s" % ri(0,45)])
		redoneAmount = 1
		while combo in alreadyChosen:
			combo = "-".join(["%s" % ri(0,45), "%s" % ri(0,45), "%s" % ri(0,45)])
			redoneAmount += 1
		alreadyChosen.append(combo)

		total += 1
		totalString = ""

		if total < 10:
			totalString = "%s    " % total
		elif total < 100:
			totalString = "%s   " % total
		elif total < 1000:
			totalString = "%s  " % total
		elif total < 10000:
			totalString = "%s " % total
		else:
			totalString = "%s" % total

		if redoneAmount < 10:
			print("%s (%s)  - %s  --  %s" % (totalString, redoneAmount, combo == inputCombo, combo))
		elif redoneAmount < 100:
			print("%s (%s) - %s  --  %s" % (totalString, redoneAmount, combo == inputCombo, combo))

		if combo == inputCombo:
			print("\nCorrectly Guessed!\n")
			endOf = timer()
			print("Guessed in %ss" % (endOf - startOf))
			done = True