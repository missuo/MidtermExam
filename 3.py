def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))
	
count = int(input("Enter the count:" ))
numberList = []
for i in range(1,count+1):
	numberList.append(recur_fibo(i))
print("NumberList: ", numberList)
print("Avg: ", sum(numberList) / len(numberList))
