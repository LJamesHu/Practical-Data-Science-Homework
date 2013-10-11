import matplotlib.pyplot as plt

# Instantiate a list
survey_data = []

# Using Traditional Split method
# Open the file
f = open("survey_multiple_choice.csv", "r")
# Iterate through the information
for line in f:
	# Add information in the line after it has white space removed and split based off of comma delimiter 
	survey_data.append(line.strip().split(','))
	survey_data[-1][2] = survey_data[-1][2].strip()
	survey_data[-1][3] = survey_data[-1][3].strip()
	survey_data[-1][4] = survey_data[-1][4].strip()

# Close the file
f.close()

# Using numpy for formatted, prettier information
import numpy as np

# Read the txt file and arrange into array of arrays
npdata = np.genfromtxt("survey_multiple_choice.csv", dtype='string', autostrip=True, delimiter=',')

# Parsing Data

# Collecting data on Unix skill
# Set up dictionary to count
unix = {1:0, 2:0, 3:0, 4:0, 5:0}

# Go through all the lines in the info
for n in range(len(npdata)):
	# Get the 3th data point of each line
	# Check against dictionary then iterate appropriate number + 1
	if npdata[n][2] == "I don\xe2\x80\x99t even understand the question":
		unix[1] += 1

	elif npdata[n][2] == 'I have no experience working in a terminal':
		unix[2] += 1

	elif npdata[n][2] == 'I have issued a few commands in a terminal based on given instructions':
		unix[3] += 1

	elif npdata[n][2] == 'I have written simple terminal commands or done some system work on the terminal':
		unix[4] += 1

	elif npdata[n][2] == 'I have written complex commands done or have done deep system work':
		unix[5] += 1

# Graph it out
fig, axes = plt.subplots()

axes.plot(unix.keys(), unix.values(), label="Unix Shell Skill Level")
axes.set_xlabel('Skill Level')
axes.set_xticks(unix.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Unix Shell Skill Level')
axes.legend();
plt.show()

# Collecting data on Database skill
# Set up dictionary to count
db = {1:0, 2:0, 3:0, 4:0, 5:0}

# Go through all the lines in the info
for n in range(len(npdata)):
	# Get the 4th data point of each line
	# Check against dictionary then iterate appropriate number + 1
	if npdata[n][3] == 'I have never directly accessed a database':
		db[1] += 1

	elif npdata[n][3] == 'I have issued simple queries to a relational database based on given instructions':
		db[2] += 1

	elif npdata[n][3] == 'I can write simple queries and issue them to a database':
		db[3] += 1

	elif npdata[n][3] == 'I can write very complex queries when needed':
		db[4] += 1

	elif npdata[n][3] == 'I am a database hacker':
		db[5] += 1

#Graph it out
fig, axes = plt.subplots()

axes.plot(db.keys(), db.values(), label="Database Skill Level")
axes.set_xlabel('Skill Level (Low to High)')
axes.set_xticks(db.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Database Skill Level')
axes.legend();
plt.show()

# Collecting data on Programming skill
# Set up dictionary to count
prog = {1:0, 2:0, 3:0, 4:0, 5:0}

# Go through all the lines in the info
for n in range(len(npdata)):
	# Get the 5th data point of each line
	# Check against dictionary then iterate appropriate number + 1
	if npdata[n][4] == 'I have never programmed before.':
		prog[1] += 1

	elif npdata[n][4] == 'I have written simple programs based on instructions or a tutorial':
		prog[2] += 1

	elif npdata[n][4] == 'I can write simple programs to accomplish tasks I encounter':
		prog[3] += 1

	elif npdata[n][4] == 'I can write complex programs am familiar with programming design patterns software testing system design and algorithms.':
		prog[4] += 1

	elif npdata[n][4] == 'I am a hacker or have senior-level programming experience':
		prog[5] += 1

# Graph it out
fig, axes = plt.subplots()

axes.plot(prog.keys(), prog.values(), label="Programming Skill Level")
axes.set_xlabel('Skill Level (Low to High)')
axes.set_xticks(prog.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Programming Skill Level')
axes.legend();
plt.show()

# Graph all on one figure
fig, axes = plt.subplots()

axes.plot(unix.keys(), unix.values(), label="Unix Shell Skill Level")
axes.plot(db.keys(), db.values(), label="Database Skill Level")
axes.plot(prog.keys(), prog.values(), label="Programming Skill Level")
axes.set_xlabel('Skill Level (Low to High)')
axes.set_xticks(unix.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Computer Disciplines Skill Level')
axes.legend();
plt.show()

# Bar Graph for Unix Shell Skill Level

fig, axes = plt.subplots()

axes.bar(unix.keys(), unix.values(), label="Unix Shell Skill Level", align='center')
axes.set_xlabel('Skill Level (Low to High)')
axes.set_xticks(unix.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Unix Shell Skill Level');
plt.show()

# Bar Graph for Database Skill Level

fig, axes = plt.subplots()

axes.bar(db.keys(), db.values(), label="Database Skill Level", align='center')
axes.set_xlabel('Skill Level (Low to High)')
axes.set_xticks(db.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Database Skill Level');
plt.show()

# Bar Graph for Programming Skill Level

fig, axes = plt.subplots()

axes.bar(prog.keys(), prog.values(), label="Programming Skill Level", align='center')
axes.set_xlabel('Skill Level (Low to High)')
axes.set_xticks(prog.keys())
axes.set_ylabel('Number of Responses')
axes.set_title('Programming Skill Level');
plt.show()