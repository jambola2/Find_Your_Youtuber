#Initial test case made at 12:53am, US Central time by Austinprog


# This is a test case for the new algorithms to possible be implemented into in due time.
# if you manage to do so please take note of it and post it in issues.
import time 
def main():
	print "Please enter the category that you would like to enter"
	comedy = raw_input()
	if comedy == "comedy":
	   print "Going to comedy!"
	   print "Test successful"
	elif comedy != "comedy":
	   print "We're sorry but you typed", comedy, "\n that is not valid. Please try again in 3 seconds"
	   time.sleep(3)
	   main()
main()
    