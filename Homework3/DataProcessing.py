# Import json reader
import json

# Used to count users/objects/responses
users = {}
objects = {}
responses = {}

# Used to count rejections of each user
userrejections = {}

# Used to count rejections to each response
responserejections = {}

# Used to count accepts of each user
useraccepts = {}

# --------------------------------------

# Open the file
with open("user_tag_activity.json") as f:
	# Iterate through every line of the file.
    for line in f:

    	# --------------------------------------

    	# Used for Question 1
    	# Used to count users, if not counted, instantiate in users
		if users.get(json.loads(line)["user"]) == None:
			users[json.loads(line)["user"]] = 1
		# Used to count objects, if not counted, instantiate in objects
		if objects.get(json.loads(line)["object"]) == None:
			objects[json.loads(line)["object"]] = 1
		# Used to count responses, if not counted, instantiate in responses
		if responses.get(json.loads(line)["response"]) == None:
			responses[json.loads(line)["response"]] = 1

		# --------------------------------------

		# Question 2
		# Filtering NULL fields
		if line.find("NULL") == -1:

			# --------------------------------------

			# Used for Question 3
    		# Finding a user's rejections and total responses.
			# Instantiate an entry with a list containing rejections and total responses if none exists
			if userrejections.get(json.loads(line)["user"]) == None:
				userrejections[json.loads(line)["user"]] = [0, 0]

			# Increment total responses
			userrejections[json.loads(line)["user"]][1] += 1

			# Increment total rejections if it is a rejection
			if json.loads(line)["accepted"] == "0":
				userrejections[json.loads(line)["user"]][0] += 1

			# --------------------------------------

			# Used for Question 4
			# Finding a response's rejections and total responses
			# Instantiate an entry with a list containing rejections and total responses if none exists
			if responserejections.get(json.loads(line)["response"]) == None:
				responserejections[json.loads(line)["response"]] = [0, 0]

			# Increment total responses
			responserejections[json.loads(line)["response"]][1] += 1

			# Increment rejections if it is a rejection
			if json.loads(line)["accepted"] == "0":
				responserejections[json.loads(line)["response"]][0] += 1

			# --------------------------------------

			# Used for Question 5 and 6
			# Finding a user's accepts and total responses.
			# Instantiate an entry with a list containing accepts and total responses if none exists
			if useraccepts.get(json.loads(line)["user"]) == None:
				useraccepts[json.loads(line)["user"]] = [0, 0]

			# Increment total responses
			useraccepts[json.loads(line)["user"]][1] += 1

			# Increment accepts if it is accepted
			if json.loads(line)["accepted"] == "1":
				useraccepts[json.loads(line)["user"]][0] += 1

			# --------------------------------------

# Close out the file
f.close()

# --------------------------------------

# Question 1

# Print the relevant unique users/objects/responses
print "There are " + str(len(users)) + " unique users."
print "There are " + str(len(objects)) + " unique objects."
print "There are " + str(len(responses)) + " unique responses."

# --------------------------------------

# Question 3

# Calculate 5 users with highest rejection rates
# Do so by sorting the user rejections using a key that made by taking their rejections and dividing it by their total responses, then returning only those with the 5 highest results.
highestuserrejrate = sorted(userrejections, key=lambda userrejrate: float(userrejections[userrejrate][0])/userrejections[userrejrate][1], reverse = True)[:5]

# Find 5 users with most rejections
# Do so by sorting the user rejections using a key that made by taking their rejections, then returning only those with the 5 highest results.
mostrej = sorted(userrejections, key=lambda usertotalrej: userrejections[usertotalrej][0], reverse=True)[:5]

# Print the results
print "The 5 users with the highest rejection rate are %s." % ", ".join(map(str, highestuserrejrate))
print "The 5 users with the greatest number of rejections are %s." % ", ".join(map(str, mostrej))

# --------------------------------------

# Question 4

# Calculate 5 responses with highest rejection rates
# Do so by sorting the response rejections using a key that made by taking the response's rejections and dividing it by the response's total responses, then returning only those with the 5 highest results.
highestresprejrate = sorted(responserejections, key=lambda resprejrate: float(responserejections[resprejrate][0])/responserejections[resprejrate][1], reverse = True)[:5]

# Print the results
print "The 5 responses with the highest rejection rate are %s." % ", ".join(map(str, highestresprejrate))

# Find the amount of good tags that would be erraneously rejected if the top 5 reponses with the highest rejection rate were rejected.
# Create var to find amount of good tags erroneously rejected
goodtagerror = 0
# Go through 5 responses with highest rejection rate
for n in highestresprejrate:
	# Add to goodtagerror the amount of responses minus the amount of rejected responses to find the amount of accepted responses for each of the responses with the highest rejection rate
	goodtagerror += responserejections[n][1]-responserejections[n][0]

# Print the results
print "The amount of accepted tags that would be erroneously rejected is " + str(goodtagerror) + "."

# --------------------------------------

# Question 5

# Find 5 users with greatest number of accepted responses
# Do so by sorting the user accepts using a key that made by taking their acceptances, then returning only those with the 5 highest results.
mostacc = sorted(useraccepts, key=lambda usertotalacc: useraccepts[usertotalacc][0], reverse=True)[:5]

# Print the results
print "The 5 users with the greatest number of accepted responses are %s." % ", ".join(map(str, mostacc))

# Create var to find amount of bad tags erroneously accepted
badtagerror = 0
# Go through 5 users with the greatest number of accepted responses
for n in mostacc:
	# Add to goodtagerror the total amount of responses minus the amount of accepted responses to find the amount of rejected responses for each of the users with the highest number of accepted tags
	badtagerror += useraccepts[n][1]-useraccepts[n][0]
	
# Print the results
print "The amount of rejected tags that would be erroneously accepted is " + str(badtagerror) + "."

# --------------------------------------

# Question 6

# Instantiate a list to hold acceptance rates
useraccrate = []

# Get all the user acceptance rates
for n in useraccepts:
	useraccrate.append(float(useraccepts[n][0])/useraccepts[n][1])

# Plot out the distribution histogram of user acceptance rates
import matplotlib.pyplot as plt

fig, axes = plt.subplots()

axes.hist(useraccrate, bins = 20)
axes.set_xlabel('User Response Acceptance Rate')
axes.set_ylabel('Number of Users')
axes.set_title('User Response Acceptance Distribution');
plt.show()

# --------------------------------------