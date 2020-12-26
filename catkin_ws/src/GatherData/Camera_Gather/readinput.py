#!/usr/bin/env python
import sys, select, termios, tty

def getKey(settings):
	tty.setraw(sys.stdin.fileno())
	rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
	if rlist:
		key = sys.stdin.read(1)
	else:
		key = ''
	
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def checkKey(key):
	if (key == "p"):
		return False
	elif (key == "r"):
		return True
	else:
		return	

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)

	record = False
	while True:
		key = getKey()
		record = checkKey(key, record)		
		

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
