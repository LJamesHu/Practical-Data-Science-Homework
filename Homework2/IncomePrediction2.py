import numpy as np

# Read the txt file and arrange into array of arrays
data = np.genfromtxt("marketing.data")

# Setup dictionary with list with two values, 1 to store cumulative income, 1 to store how many people
eduactual = {1.0:[0,0], 2.0:[0,0], 3.0:[0,0], 4.0:[0,0], 5.0:[0,0], 6.0:[0,0]}

# The given education income modifiers
eduincmod = {1.0:-3, 2.0:-1, 3.0:0, 4.0:1, 5.0:3, 6.0:4}

# Go through all the lines in the file
for n in range(len(data)):
	# Get the 5th data point of each line
	# Check if legitimate (not nan)
	if data[n][4] > 0 and data[n][0] > 0:
		# Add income level to the income list
		eduactual[data[n][4]][0] += data[n][0]
		# Iterate +1 to account for another person
		eduactual[data[n][4]][1] += 1

# Set default incomes
incomeactual = {1.0:0, 2.0:0, 3.0:0, 4.0:0, 5.0:0, 6.0:0}

# Iterate through and get average income for each education level.
for n in eduactual:
	incomeactual[n] = eduactual[n][0]/eduactual[n][1]

print "Actual Income Level per Education Level: " + str(incomeactual)

# Set default incomes
incomeprojected = {1.0:4, 2.0:4, 3.0:4, 4.0:4, 5.0:4, 6.0:4}

# Iterate through and get projected income for each education level
for n in eduincmod:
	incomeprojected[n] += eduincmod[n]

print "Projected Income Level per Education Level: " + str(incomeprojected)

# Create dict
incomediff = {1.0:0, 2.0:0, 3.0:0, 4.0:0, 5.0:0, 6.0:0}

# Iterate through and get difference for each education level
for n in incomeprojected:
	incomediff[n] = incomeactual[n] - incomeprojected[n]

print "The total difference between actual and predicted income level at each education level is: " + str(incomediff)

# Create value to measure average difference
avgdiff = 0

# Iterate through and sum the differences for each education level
for n in incomediff:
	avgdiff += incomediff[n]

# Get the average
avgdiff = avgdiff/6

print "The average difference per user between actual and predicted income level at each education level is: " + str(avgdiff)

# Question 2


# Getting the income actual total
incomeactual2total = {}
# Getting the income actual count
incomeactual2count = {}

# Go through all the lines in the file
for n in range(len(data)):
	# Check if legitimate (not nan)
	if data[n][4] > 0 and data[n][5] > 0 and data[n][0] > 0:
		# Check if exists in dictionary
		if incomeactual2total.get((data[n][4],data[n][5])) == None:
			# If not instantiate in total and count
			incomeactual2total[data[n][4],data[n][5]] = 0
			incomeactual2count[data[n][4],data[n][5]] = 0
		# Add income level to the income list
		incomeactual2total[(data[n][4],data[n][5])] += data[n][0]
		# Iterate +1 to account for another person
		incomeactual2count[(data[n][4],data[n][5])] += 1

# Instantiate Averages
incomeactual2average = {}

# Calculate average actual income level per education level and occupation combination
for n in incomeactual2total:
	incomeactual2average[n] = incomeactual2total[n]/incomeactual2count[n]


# Getting projected income with both income modifiers
incomeprojected2 = {}

# The given occupation income modifiers
ocuincmod = {1.0:2.5, 2.0:0.6, 3.0:0.0, 4.0:0.2, 5.0:-0.5, 6.0:-1.5, 7.0:0.3, 8.0:0.8, 9.0:-2.5}

# Iterate through education income modifiers
for n in eduincmod:
	# Iterate through occupation income modifiers
	for m in ocuincmod:
		# Find projected income by using relevant education and occupation modifiers, adding the base of 4
		incomeprojected2[n,m] = eduincmod[n] + ocuincmod[m] + 4

incomediff2 = {}

# Iterate through and get difference for each education level
for n in incomeactual2average:
	incomediff2[n] = incomeactual2average[n] - incomeprojected2[n]

print "The total difference between actual and predicted income level at each combination of education level and occupation is: " + str(incomediff2)

# Create value to measure average difference
avgdiff2 = 0
diffcount2 = 0

# Iterate through and sum the differences for each education level
for n in incomediff2:
	avgdiff2 += incomediff2[n]
	diffcount2 += 1

# Get the average
avgdiff2 = avgdiff2/diffcount2

print "The average difference per user between actual and predicted income level at each education level is: " + str(avgdiff2)