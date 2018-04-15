#!/usr/bin/python
import hashlib
import sys
import itertools
from datetime import datetime,time
now = datetime.now()

ihash = sys.argv[1]
wordlist = sys.argv[2]
def hash(input):
	input = str(input)
	hash = hashlib.md5()
	hash.update(input.encode("utf-8"))
	return hash.hexdigest()

def crack(ihash):
	total = sum(1 for line in open(wordlist))
	lines = [line.rstrip('\n') for line in open(wordlist)]
	f = open("cracks.txt","a")
	n = str(total) + " passwords loaded\n"
	print n
	a = "Attempting bruteforce attack for " + ihash + "\n"
	f.write(n)
	print a
	f.write(a)
	for word in lines:
		whash = hash(str(word))
		if(whash == ihash):
			m = "Match Found!!! :" + word
			print m
			f.write(m)
			time = (datetime.now() - now).seconds
			t = "Time elapsed :" + str(time) + " seconds"
			print t
			f.write(t)
			with open(wordlist) as myFile:
				for num, line in enumerate(myFile, 1):
					if word in line:
						p = 'Total words tried:' + str(num)
						print p
						f.write(p)
						speed = num/time
						speed = round(speed,0)
						speed = str(speed).replace(".0","")
						print "Estimated speed: " + speed + " words per second"
						exit()
		else:
			t = "trying " + word + "\n"
			print t
			f = open("cracks.txt","a")
			f.write(t)

crack(ihash)