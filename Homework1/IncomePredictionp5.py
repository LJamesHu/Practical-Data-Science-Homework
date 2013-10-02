import numpy as np
import matplotlib.pyplot as pl

# Read the txt file and arrange into array of arrays
data = np.loadtxt("marketingdatap3.txt")
# Set up dictionary to count
inc = {1.0:0, 2.0:0, 3.0:0, 4.0:0, 5.0:0, 6.0:0, 7.0:0, 8.0:0, 9.0:0}

# Go through all the lines in the file
for n in range(len(data)):
	# Check if they have done some grad school (6.0) on education (5th column of each line)
	if data[n][4] == 6.0:
		# Given that they are, get the 1st data point of that line (income)
		# Check against dictionary then iterate + 1
		inc[data[n][0]] += 1

# Show distribution
print inc

# Plot distribution as bars
pl.bar(range(len(inc)), inc.values(), align='center')
pl.xticks(range(len(inc)), inc.keys())

pl.show()