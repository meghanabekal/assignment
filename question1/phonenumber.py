# Python program to check if
# given mobile number is valid
import re
import sys

def isValid(s):
	Pattern = re.compile("^\+?\d{0,3}[-\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}?")
	return Pattern.match(s)

while(1):
	s = input("Enter the phone number : ")
	if (isValid(s)):
		print ("Valid Number")	
	else :
		print ("Invalid Number")
	print("==========================")
	print("Enter any key to continue")
	print("Enter 2 to End the program")
	print("==========================")
	n=input()
	if(n=="2"):
		break;

