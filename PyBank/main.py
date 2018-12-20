# Modules
import os
import csv


# Set path for input file read
csvpath = os.path.join("..", "Resources", "budget_data.csv")


# Specify the file to write to
outfile = '../Resources/PyBankoutput.txt'

# Iniitialize variables
totalmonths = 0
totalamt = 0

# open the csv file
with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	linecount = 0
	
    
# Loop through the file and  determine total amt , max increase , decrease .
	for row in csvreader:
		if linecount == 0:
			currentamt = 0
			lastamtchange = 0
			curramtchange = 0
			maxincreasemonth = ''
			maxincreaseamt = 0
			maxdecreasemonth = ''
			maxdecreaseamt = 0
		
		else:
			currentamt = int(row[1])
			totalmonths = totalmonths + 1
			totalamt = totalamt + currentamt
			curramtchange = currentamt - lastamt
			if linecount == 1:
				#store first row amt
				firstrowamt = currentamt
			else:
				if curramtchange > maxincreaseamt:
					maxincreaseamt = curramtchange 
					maxincreasemonth = (row[0])
				
				if curramtchange < maxdecreaseamt:
					maxdecreaseamt = curramtchange
					maxdecreasemonth = (row[0])
			
		lastamt = currentamt
		linecount += 1

	#store the last row amt
	lastrowamt = currentamt

	#calculate average change
	averagechange = round((lastrowamt - firstrowamt ) / (totalmonths - 1),2)

	#print the values to terminal
	print("Total Months: " + str(totalmonths))
	print("Total: " +"$"+ str(totalamt))
	print("Average Change: " +"$"+ str(averagechange))
	print("Greatest Increase in Profits: "+ str(maxincreasemonth) + " ($" + str(maxincreaseamt) + ")")
	print("Greatest Decrease in Profits: "+ str(maxdecreasemonth) + " ($" + str(maxdecreaseamt) + ")")
	


	# Open the file using "write" mode. Specify the variable to hold the contents
with open(outfile, 'w') as file:
	file.write("Total Months: "  + str(totalmonths) + "\n")
	file.write("Total: "  +"$"+ str(totalamt) + "\n")
	file.write("Average Change: " +"$"+ str(averagechange) + "\n")
	file.write("Greatest Increase in Profits: "+ str(maxincreasemonth) + " ($" + str(maxincreaseamt) + ")\n")
	file.write("Greatest Decrease in Profits: "+ str(maxdecreasemonth) + " ($" + str(maxdecreaseamt) + ")\n")
		


