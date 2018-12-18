# Modules
import os
import csv


# Set path for input file read
csvpath = os.path.join("..", "Resources", "budget_data.csv")


# Specify the file to write to
outfile = '../Resources/PyBankoutput.txt'

totalmonths = 0
totalamt = 0

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	linecount = 0
	
    
# Loop through looking for the video
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


	lastrowamt = currentamt
	averagechange = round((lastrowamt - firstrowamt ) / (totalmonths - 1),2)

	print("total months" + str(totalmonths))
	print("total amount" + str(totalamt))
	print("average change" + str(averagechange))
	print("maximum increase"+ str(maxincreaseamt))
	print("maximum increase month"+ str(maxincreasemonth))
	print("maximum decrease"+ str(maxdecreaseamt))
	print("maximum decrease month"+ str(maxdecreasemonth))


	# Open the file using "write" mode. Specify the variable to hold the contents
with open(outfile, 'w') as file:
	file.write("total months" + str(totalmonths) + "\n")
	file.write("total amount" + str(totalamt) + "\n")
	file.write("average change" + str(averagechange) + "\n")
	file.write("maximum increase"+ str(maxincreaseamt) + "\n")
	file.write("maximum increase month"+ str(maxincreasemonth) + "\n")
	file.write("maximum decrease"+ str(maxdecreaseamt) + "\n")
	file.write("maximum decrease month"+ str(maxdecreasemonth) + "\n")


