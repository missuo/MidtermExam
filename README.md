```python
# @About   : Midterm Exam Part 2
# @Author  : Vincent Young(Yang YingTao)
# @ID      : 1922542
# @Email   : i@yyt.moe
# @Github  : https://github.com/missuo  
# @Time    : Friday, October 22, 2021 (GMT+8)
```


```python
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

# Check if Area's input is legal
while True:
	area = input("Enter the area of wall space: ")
	if(is_number(area) == True and float(area) > 0):
		area = float(area)
		break
	else:
		print("Wrong input, please re-enter.")

# Check if wallType's input is legal
while True:
	wallType = input("Enter indoor or outdoor: ")
	if(wallType == 'indoor' or wallType == 'outdoor'):
		break
	else:
		print("Wrong input, please re-enter.")

# Define some variables to be used
perHourSalary = 40
if(wallType == 'indoor'):
	perGallonArea = 120
	perGallonTime = 8 
	perGallonPrice = 30
elif(wallType == 'outdoor'):
	perGallonArea = 100
	perGallonTime = 10
	perGallonPrice = 35

# Enter the computing section
paintCapacityActual = area / perGallonArea

# When paint is less than one gallon, purchase one gallon
if(area % perGallonArea == 0):
	paintCapacityNeedBuy = paintCapacityActual
else:
	paintCapacityNeedBuy = area // perGallonArea + 1
timeConsuming = perGallonTime * paintCapacityActual
paintTotalPrice = paintCapacityNeedBuy * perGallonPrice
totalSalary = perHourSalary * timeConsuming
totalCost = totalSalary + paintTotalPrice

# Return results
print("Number of gallons of print required: ", format(paintCapacityNeedBuy, ".2f"))
print("Number of labor hours required: ", format(timeConsuming, ".2f"))
print("Cost of the paint: ", format(paintTotalPrice, ".2f"))
print("Labor charges: ", format(totalSalary, ".2f"))
print("Total cost: ", format(totalCost, ".2f"))

```

    Enter the area of wall space: 180
    Enter indoor or outdoor: indoor
    Number of gallons of print required:  2.00
    Number of labor hours required:  12.00
    Cost of the paint:  60.00
    Labor charges:  480.00
    Total cost:  540.00



```python
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
			
```

    Please enter your score1:100
    Please enter your score2:90
    Please enter your score3:99
    Please enter your score4:70
    Please enter your score5:80
    Your level for this test is B



```python

```
