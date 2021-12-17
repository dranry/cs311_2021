#	Daniel Raney
#	Final Project 
#	Sorting algorithm implementation and stats testing
#	List so far: 
#	Bubble Sort
#	Merge Sort
import random
import time


def copyArray(copyingArray):
	retArray = []
	for i in copyingArray:
		tempArr = []
		for j in i:
			tempArr.append(j)	
		retArray.append(tempArr)
	return retArray

def makeData():#data):
	data = []
	appendArray = []
	for i in range(0,50):
		appendArray = []
		for j in range(0,(i + 1) * 100):
		#for j in range(0,(i + 1) * 5):
			appendArray.append((random.randint(1,1000)))
		data.append(appendArray)
	return data

def doBubbleSort(data):
	workingArr = data
	timeArr = []
	for element in workingArr:
		start = time.process_time()
		print(str(len(element)) + " starts at " + str(start))
		while True:
			notSwapped = True
			for i in range(0, len(element) - 1):
				first = element[i]
				second = element[i + 1]
				if first > second:
					element[i] = second
					element[i + 1] = first
					notSwapped = False
			if notSwapped:
				break
		print(str(len(element)) + " ends at " + str(start))
		end = time.process_time()
		timeArr.append(end - start)
	return timeArr

def doMergeSort(workingArr):
	timeArr = []
	for i in range(0, len(workingArr)):
		start = time.process_time()
		print(str(len(workingArr[i])) + " elements starts at " + str(start))
		
		workingArr[i] = mergeSort(workingArr[i])

		end = time.process_time()
		print(str(len(workingArr[i])) + " elements ends at " + str(end))
		timeArr.append(end - start)
	return timeArr

def mergeSort(workingArr):
	if len(workingArr) <= 1:
		return workingArr
	right = []
	left = []
	if len(workingArr) % 2 == 1:
		midpoint = (len(workingArr) // 2) + 1
	else:
		midpoint = len(workingArr) // 2
	for i in range(0, midpoint):
		left.append(workingArr[i])
	for i in range(midpoint, len(workingArr)):
		right.append(workingArr[i])
	left = mergeSort(left)
	right = mergeSort(right)
	return merge(left, right)
		
def merge(arr1, arr2):
	length1 = len(arr1)# - 1
	length2 = len(arr2)# - 1
	finalArr = []
	i = 0
	j = 0
	while(i < length1 and j < length2):
		if(arr1[i] < arr2[j]):
			finalArr.append(arr1[i])
			i += 1
		else:
			finalArr.append(arr2[j])
			j += 1
	for x in range(i, length1):
		finalArr.append(arr1[x])
	for y in range(j, length2):
		finalArr.append(arr2[y])
	return finalArr	
#############

sortData = makeData()
print("Bubble Sort")
bubbleData = copyArray(sortData)
bubbleTime = doBubbleSort(bubbleData)

print("//////////\nMerge Sort:")
mergeData = copyArray(sortData)
mergeTime = doMergeSort(mergeData)

print("Bubble Sort:")
for i in range(0, len(bubbleData)):
	print(str(len(bubbleData[i])) + " elements took " + str(bubbleTime[i]) + " seconds")
print("Merge Sort:")
for j in range(0, len(mergeData)):
	print(str(len(mergeData[j])) + " elements took " + str(mergeTime[j]) + " seconds")
