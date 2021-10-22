# Define a function to determine if it is a number
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
		
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
		
	return False

# Define a function to calculate the level
def testAverage(scoreList):
	averageScore = sum(scoreList) / len(scoreList)
	if(averageScore >= 90 and score <= 100):
		return 'A'
	elif(averageScore >= 80):
		return 'B'
	elif(averageScore >= 70):
		return 'C'
	elif(averageScore >= 60):
		return 'D'
	else:
		return 'E'

# Define main function
def main():
	# Define a Score List
	scoreList = []
	# Loop to get five scores of five inputs
	for i in range(5):
		# Determine if the entered score is legal
		while True:
			score = input("Please enter your score" + str(i+1) + ":")
			if(is_number(score) == True and float(score) >= 0 and float(score) <= 100):
				score = float(score)
				scoreList.append(score)
				break
			else:
				print("Wrong input, please re-enter.")
	# Call the testAverage function and assign the return result to the level variable
	level = testAverage(scoreList)
	# Print result
	print("Your level for this test is", level)

if __name__ == "__main__":
	main()
