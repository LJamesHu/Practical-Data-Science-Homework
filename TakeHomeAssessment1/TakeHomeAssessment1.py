# Import json reader
import json
# Import numpy for mean/standard deviation
import numpy as np
# Import pyplot for plotting
import matplotlib.pyplot as plt

# Used for Question b
# Count names to see if there are any duplicate names
names = {}
dupnames = {}

# Used for Question c
# Counter for instances of missing data
missingdata = 0

# Used for Question d
# Dictionaries to get values and frequency
RFA2F = {}
RFA2A = {}

# Used for Question e
# Dictionary to get values and frequency
TARGETB = {0:0, 1:0}

# Used for Question f, g
# Array of Wealth given response
Wealth0 = []
Wealth1 = []

# Used for Question h, i, j
# Array to be manipulated to display records by name field
RecordsList = []

# --------------------------------------

# Open the file
with open("assess1_data.json") as f:
	# Iterate through every line of the file.
    for line in f:

    	# --------------------------------------

    	# Used for Question b

    	# Used to count names, if not counted, instantiate in names
    	if names.get(json.loads(line)["NAME"]) == None:
			names[json.loads(line)["NAME"]] = 1
        # If it is not None, then the name has already been counted, which means that the name is a duplicate
        else:
            dupnames[json.loads(line)["NAME"]] = 1

        # --------------------------------------

        # Used for Question c
        # If it has -9999 fields
        if line.find("-9999") != -1:
            # Count number of -9999 fields
            missingdata += 1

        # Otherwise given no -9999 fields
        else:
            # --------------------------------------

            # Used for Question d

            # Used to count RFA_2F values, if not counted, instantiate in RFA2F
            if RFA2F.get(json.loads(line)["RFA_2F"]) == None:
                RFA2F[json.loads(line)["RFA_2F"]] = 1
            # Otherwise if already in, just increment existing key by 1
            else:
                RFA2F[json.loads(line)["RFA_2F"]] += 1

            # Used to count RFA_2A values, if not counted, instantiate in RFA2A
            if RFA2A.get(json.loads(line)["RFA_2A"]) == None:
                RFA2A[json.loads(line)["RFA_2A"]] = 1
            # Otherwise if already in, just increment existing key by 1
            else:
                RFA2A[json.loads(line)["RFA_2A"]] += 1

            # --------------------------------------

            # Used for Question e

            # Otherwise if already in, just increment existing key by 1
            TARGETB[json.loads(line)["TARGET_B"]] += 1

            # --------------------------------------

            # Used for Question f, g

            # If the person did not respond
            if json.loads(line)["TARGET_B"] == 0:
                # Add their wealth index to the nonresponders wealth array
                Wealth0.append(json.loads(line)["WEALTH_INDEX"])
            # Otherwise they did
            else:
                # Add their wealth index to the responders wealth array
                Wealth1.append(json.loads(line)["WEALTH_INDEX"])

            # --------------------------------------

            # Used for question h, i, j

            # Add line to array to be sorted later
            RecordsList.append(line)

            # --------------------------------------

# --------------------------------------

# Question b

# Print out the duplicate names
print dupnames.keys()

# --------------------------------------

# Question c

# Print number of -9999 fields
print missingdata

# --------------------------------------

# Question d

# Print values and frequency of RFA_2F
print RFA2F

# Print values and frequency of RFA_2A
print RFA2A

# --------------------------------------

# Question e

# Print values and frequency of TARGET_B
print TARGETB

# Print proportion of targeted consumers that responded
print TARGETB[1]/float(TARGETB[0]+TARGETB[1])

# --------------------------------------

# Question f

# Show the mean and standard deviations as measure of distribution
print "Wealth Index Given No Response"
print "The average customer's wealth index given no response is " + str(np.mean(Wealth0))
print "The standard deviation of a customer's wealth index given no response is " + str(np.std(Wealth0))

# Plot out the distribution histogram of a customer's wealth index given no response
fig0, axes0 = plt.subplots()

axes0.hist(Wealth0, bins = 20)
axes0.set_xlabel('Wealth Index')
axes0.set_ylabel('Number of Customers')
axes0.set_title('Wealth Index Given No Response');
plt.show()

print "========================"

# Show the mean and standard deviations as measure of distribution
print "Wealth Index Given Response"
print "The average customer's wealth index given response is " + str(np.mean(Wealth1))
print "The standard deviation of a customer's wealth index given response is " + str(np.std(Wealth1))

# Plot out the distribution histogram of a customer's wealth index given response
fig1, axes1 = plt.subplots()

axes1.hist(Wealth1, bins = 20)
axes1.set_xlabel('Wealth Index')
axes1.set_ylabel('Number of Customers')
axes1.set_title('Wealth Index Given Response');
plt.show()

# --------------------------------------

# Question g

# Plot out the distribution histogram of a customer's wealth index
figboth, axesboth = plt.subplots()

axesboth.hist([Wealth0, Wealth1], bins = 20)
axesboth.set_xlabel('Wealth Index')
axesboth.set_ylabel('Number of Customers')
axesboth.set_title('Wealth Index of Customers');
plt.show()

# Plot out the distribution histogram of a customer's wealth index
figboth2, axesboth2 = plt.subplots()

axesboth2.hist([Wealth0, Wealth1], bins = 20, normed = True)
axesboth2.set_xlabel('Wealth Index')
axesboth2.set_ylabel('Number of Customers %')
axesboth2.set_title('Wealth Index of Customers %');
plt.show()

# --------------------------------------

# Question h

# Used sorted to organize list of records by NAME field. Display results 0 - 10.
print sorted(RecordsList, key=lambda name: json.loads(name)["NAME"])[0:10]

# Display results 20,000 - 20,010
print sorted(RecordsList, key=lambda name: json.loads(name)["NAME"])[20000:20010]

# --------------------------------------

# Question i

# Used sorted to organize list of records by NAME field, which is then split to grab the last name. Display results 0 - 10.
print sorted(RecordsList, key=lambda name: json.loads(name)["NAME"].split()[-1])[0:10]

# Display results 20,000 - 20,010
print sorted(RecordsList, key=lambda name: json.loads(name)["NAME"].split()[-1])[20000:20010]

# --------------------------------------

# Question j

# Used sorted to organize list of records by the predictive model field
PredictiveModel = sorted(RecordsList, key=lambda name: -40 + 0.8*json.loads(name)["WEALTH_INDEX"] + 0.12*json.loads(name)["RFA_2F"], reverse = True)

# Create a lambada through which the model can take a value
Model = lambda x: -40 + 0.8*json.loads(PredictiveModel[x])["WEALTH_INDEX"] + 0.12*json.loads(PredictiveModel[x])["RFA_2F"]

# Use a for loop the print the top 10 consumer records and their score from the predictive model
for record in range(0,10):
    print PredictiveModel[record] + str(Model(record))

# --------------------------------------