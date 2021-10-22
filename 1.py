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
