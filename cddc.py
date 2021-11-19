#!/bin/python3

# Catenative Doomsday Dice Cascader
# As featured in https://www.homestuck.com/extras/20

# Command line options:
# --quick (no delays, only show dice result lines)
# --resultonly (only output the final damage total. overrides --quick)
# --machinereadable (output a list of all the dice results without any formatting prettiness. overrides --quick and --resultonly)
# --wasp (maximum disappointment due to Professor Wasp's meddling. always prime bubble 6, always final result 1)

# This code is tab-indented, the way God intended.

import sys
import random
import locale
import time
import math

locale.setlocale(locale.LC_ALL, '')
sleeptime = 1.5

def main():
	# read options, call dice roller, output as requested
	opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]
	quick = False
	resultonly = False
	machinereadable = False
	wasp = False
	if "--quick" in opts:
		quick = True
	if "--resultonly" in opts:
		resultonly = True
	if "--machinereadable" in opts:
		machinereadable = True
	if "--wasp" in opts:
		wasp = True
	results = diceroller(wasp)
	if machinereadable:
		print(results)
		quit()
	if resultonly:
		print(locale.format_string("%d", results[-1], grouping=True)+ " damage")
		quit()
	if quick:
		print("Prime Bubble (1d6): " + str(results[0]))
		diesize = 6
		if results[0] > 1:
			print("First Cascader (1d" + str(diesize) + "): " + locale.format_string("%d", results[1], grouping=True))
			diesize = diesize * results[1]
		if results[0] > 2:
			print("Second Cascader (1d" + str(diesize) + "): " + locale.format_string("%d", results[2], grouping=True))
			diesize = diesize * results[2]
		if results[0] > 3:
			print("Third Cascader (1d" + str(diesize) + "): " + locale.format_string("%d", results[3], grouping=True))
			diesize = diesize * results[3]
		if results[0] > 4:
			print("Fourth Cascader (1d" + str(diesize) + "): " + locale.format_string("%d", results[4], grouping=True))
			diesize = diesize * results[4]
		if results[0] > 5:
			print("Fifth Cascader (1d" + str(diesize) + "): " + locale.format_string("%d", results[5], grouping=True))
			diesize = diesize * results[5]
		print("Doomsday Cascader (1d" + str(diesize) + "): " + locale.format_string("%d", results[-1], grouping=True))
		quit()
	# begin default slow mode
	slowprint("> Strike using awesome dice-based technology.")
	time.sleep(sleeptime)
	print()
	print("You always knew it would come down to this.")
	time.sleep(sleeptime)
	print("You prepare the CATENATIVE DOOMSDAY DICE CASCADER,", end="", flush=True)
	time.sleep(sleeptime)
	print(" featuring loathsome POPAMATIC BUBBLE TECHNOLOGY.")
	time.sleep(sleeptime)
	print()
	input("You press the PRIME BUBBLE at the center of the machine. (Press ENTER.)")
	print("*pop*")
	time.sleep(sleeptime)
	print("The prime bubble rolled a " + str(results[0]) + "!")
	time.sleep(sleeptime)
	if results[0] == 1:
		print()
		print("How incredibly disappointing! A single DOOMSDAY CASCADER BUBBLE is allocated to one of the empty CATENATOR CRUCIBLES in the machine.")
	elif results[0] <= 3:
		print()
		print("Not a great result, but it could be worse. A set of " + str(results[0]) + " CASCADER BUBBLES is allocated to the empty CATENATOR CRUCIBLES in the machine.") 
		time.sleep(sleeptime)
		print()
		print("You begin pressing the cascader bubbles one at a time, as their results grow the dice of each successive cascader!")
	elif results[0] <= 5:
		print()
		print("A set of " + str(results[0]) + " CASCADER BUBBLES is allocated to the empty CATENATOR CRUCIBLES in the machine.")
		time.sleep(sleeptime)
		print()
		print("You begin pressing the cascader bubbles one at a time, as their results grow the dice of each successive cascader!")
	else:
		print()
		print("The most favorable result! A full set of " + str(results[0]) + " CASCADER BUBBLES is allocated to the empty CATENATOR CRUCIBLES in the machine.")
		time.sleep(sleeptime)
		print()
		print("You begin pressing the cascader bubbles one at a time, as their results grow the dice of each successive cascader!")
	diesize = 6
	if results[0] > 1:
		print()
		input("You press the FIRST CASCADER BUBBLE (1d" + str(diesize) + "). (Press ENTER.)")
		print("*pop*")
		time.sleep(sleeptime)
		print("The first cascader rolled a " + locale.format_string("%d", results[1], grouping=True) + "!")
		diesize = diesize * results[1]
	if results[0] > 2:
		print()
		input("You press the SECOND CASCADER BUBBLE (1d" + str(diesize) + "). (Press ENTER.)")
		print("*pop*")
		time.sleep(sleeptime)
		print("The second cascader rolled a " + locale.format_string("%d", results[2], grouping=True) + "!")
		diesize = diesize * results[2]
	if results[0] > 3:
		print()
		input("You press the THIRD CASCADER BUBBLE (1d" + str(diesize) + "). (Press ENTER.)")
		print("*pop*")
		time.sleep(sleeptime)
		print("The third cascader rolled a " + locale.format_string("%d", results[3], grouping=True) + "!")
		diesize = diesize * results[3]
	if results[0] > 4:
		print()
		input("You press the FOURTH CASCADER BUBBLE (1d" + str(diesize) + "). (Press ENTER.)")
		print("*pop*")
		time.sleep(sleeptime)
		print("The fourth cascader rolled a " + locale.format_string("%d", results[4], grouping=True) + "!")
		diesize = diesize * results[4]
	if results[0] > 5:
		print()
		input("You press the FIFTH CASCADER BUBBLE (1d" + str(diesize) + "). (Press ENTER.)")
		print("*pop*")
		time.sleep(sleeptime)
		print("The fifth cascader rolled a " + locale.format_string("%d", results[5], grouping=True) + "!")
		diesize = diesize * results[5]
	time.sleep(sleeptime)
	print()
	print("The final DOOMSDAY CASCADER is ready.")
	time.sleep(sleeptime)
	if diesize < 1000:
		print("This will trigger the weapon on the terrible device and potentially deal up to " + locale.format_string("%d", diesize, grouping=True) + " hit points in damage!")
	else:
		# theoretical max is 6^32 = 7,958,661,109,946,400,884,391,936, so we don't need to check more than septillions
		big_value = diesize
		thousands_count = 0
		while big_value > 1000:
			big_value = big_value / 1000
			thousands_count = thousands_count + 1
		big_value = math.floor(big_value)
		sizestring = ""
		if thousands_count == 1: sizestring = "THOUSAND"
		elif thousands_count == 2: sizestring = "MILLION"
		elif thousands_count == 3: sizestring = "BILLION"
		elif thousands_count == 4: sizestring = "TRILLION"
		elif thousands_count == 5: sizestring = "QUADRILLION"
		elif thousands_count == 6: sizestring = "QUINTILLION"
		elif thousands_count == 7: sizestring = "SEXTILLION"
		else: sizestring = "SEPTILLION"
		print("This will trigger the weapon on the terrible device and potentially deal OVER " + str(big_value) + " " + sizestring + " HIT POINTS IN DAMAGE!")
	time.sleep(sleeptime)
	input("There's only one thing left to do. (Press ENTER.)")
	print("*pop*")
	time.sleep(sleeptime)
	print()
	print("You hear a loud rumbling sound, and then bolts of blue lightning begin shooting out of the machine, striking its target!")
	time.sleep(sleeptime)
	print()
	if results[-1] < 10:
		print("The piece of junk hits for just " + locale.format_string("%d", results[-1], grouping=True) + " damage.")
		time.sleep(sleeptime)
		print("What a waste...")
	elif results[-1] < 10000:
		print("The Catenative Doomsday Dice Cascader hits for " + locale.format_string("%d", results[-1], grouping=True) + " damage!")
	elif results[-1] < 1000000000:
		print("The Catenative Doomsday Dice Cascader hits for a whopping " + locale.format_string("%d", results[-1], grouping=True) + " points of damage!")
	else:
		print("The Catenative Doomsday Dice Cascader hits for a jaw-dropping " + locale.format_string("%d", results[-1], grouping=True) + " points of damage!")
		time.sleep(sleeptime)
		print("Whatever you were aiming at, it's gone now!")

def diceroller(wasp):
	# roll dice, cause doomsday (maybe). return a list of the results.
	diesize = 6
	results = []
	primebubble = random.randint(1,6)
	if wasp: primebubble = 6
	results.append(primebubble)
	for i in range(0,primebubble):
		cascader = random.randint(1,diesize)
		results.append(cascader)
		diesize = diesize * cascader
	if wasp: results[-1] = 1
	return results

def slowprint(text):
	for c in text:
		print(c, end="", flush=True)
		time.sleep(0.1)
	print()

if __name__=="__main__":
    main()
