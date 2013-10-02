import numpy as np

# Read the txt file and arrange into array of arrays
data = np.loadtxt("marketingdatap3.txt")
# Set up dictionary to count
edu = {1.0:0, 2.0:0, 3.0:0, 4.0:0, 5.0:0, 6.0:0}

# Go through all the lines in the file
for n in range(len(data)):
	# Get the 5th data point of each line
	# Check against dictionary then iterate + 1
	edu[data[n][4]] += 1

# Find which value is highest (most represented) by searching through the dictionary for the highest value.
print max(edu, key=edu.get)