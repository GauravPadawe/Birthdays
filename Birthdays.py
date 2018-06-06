a = ""   # Passing Empty String

def birthday(x):                                  # Defining Procedure
	import time                                   # Importing time from Library
	birthdays = {                                 # Given Dictionary
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955',
	     "Bill Gates": "28/10/1955",
	     "Steve Jobs": "24/2/1955",
	     }
	x = input("Type 'Start' to begin: ")                         # To make it more Interactive I had assigned a input value to be "Start" to begin dictionary
	if x == "Start":                                             # If value in x will be "Start", Dictionary will proceed ahead"
		print ("Welcome to B'day, let me show you what we got")  # Begins with Welcome statement
		time.sleep(1)                                            # We'll delay the O/P by passing sleep function
		for i in birthdays:                                      # for i (Individual values of birthdays) 
			print (i)                                            # Print all values by 0.5 seconds delay
			time.sleep(0.5)
		time.sleep(1)                                            # Delaying next statement by 1 second
		a = input("We have these people in dictionary, whose B'date you want to know? ")   # a will accept the user input(as a perons name) for the birthdate user wants to know
		if a in birthdays:                                                # If value passed by user is in birthdays dictionary
			print ("The birthday of " + a + " is " + birthdays[a])        # Print out its birthdate
		else:
			print ("Sorry we don't have the person in our dictionary")    # Else print out that it is not in out dictionary
	else:                                                                 
		print ("Please Re-Check - 'Start' to begin")             # This else statement is of beginning "If" statement where we wanted user to type "Start" to begin dictionary
		
print (birthday(a))

# CODED BY - GAURAV PADAWE