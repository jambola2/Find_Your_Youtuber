#Tested and approved ny austinprog. Will be pushed to Version V0.02-Alpha on TBA


def Main():
	print "Please enter the category that you would like to enter"
	selection  = raw_input()
	if selection == "comedy".lower() or selection ==  "gaming".lower():
		if selection == "comedy".lower():
				print "Going to comedy!"
				time.sleep(1) # Thos is so that the program looks neat for the user, even though its NON-GUI  want it to look as neat as possible 
				FindComedy() # Goes to comedy module 
        if selection == "gaming".lower():
			print "going to gaming!"
			time.sleep(1)
			FindGamers()
	elif selection != "comedy" .lower()  and  selection != "gaming".lower():
		print "UH OH, you typed",selection, "You were to typein comedy or gaming please try again"
		time.sleep(1)
		Main()
