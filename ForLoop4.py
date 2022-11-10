print("---------------------------------------")
#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def replaceNumber(arr):
    for i in range (0,len(arr)):
        if arr[i]>0:
            arr[i]="big"
       
    print(arr)
replaceNumber([-1,3,5,-5])

print("---------------------------------------")
#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def replacePositive(arr):
    countelement = 0
    for i in range (0,len(arr)):
        if arr[i]>0:
            countelement = countelement+1

    length = len(arr)
    arr[i-length] = countelement
    print(arr)
    
replacePositive([-1,1,1,1])
print("---------------------------------------")
#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sumValues(arr):
    sum=0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
    return sum
resultOfSum = sumValues([1,2,3,4])
print(resultOfSum)

print("---------------------------------------")
#Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5
def calcAverage(arr):
    sum=0
    for i in range(0,len(arr)):
        sum = sum+arr[i]
    avarage = sum / len(arr)
    return avarage
resultOfAverage = calcAverage([1,2,3,4])
print(resultOfAverage)

print("---------------------------------------")
#Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def calcLengthOfList(arr):
    return len(arr)
lenOfarray = calcLengthOfList([1,2,3,4])
print(lenOfarray)
print("---------------------------------------")
#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
#  If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def fimMinimumNumber(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1] :
            minmumNumber = arr[i]
        elif len(arr) == 0:
            return "False"
    return minmumNumber
min = fimMinimumNumber([7,2,4,-9])
print(min)

print("---------------------------------------")
#Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def fimMaxmumNumber(arr):
    maxmumNumber = arr[0]
    for i in arr:
        if i>maxmumNumber :
            maxmumNumber = i
        if len(arr) == 0:
            return "false"
    return maxmumNumber
max = fimMaxmumNumber([37,2,1,-9])
print(max)

print("---------------------------------------")
#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
listInfo = {'sumTotal':1, 'average':1, 'minimum':1 , 'maximum':1,'length':1 }
def indexInfo(arr):
    listInfo['sumTotal'] = sumValues(arr)
    listInfo['average'] = calcAverage(arr)
    listInfo['minimum'] = fimMinimumNumber(arr)
    listInfo['maximum'] = fimMaxmumNumber(arr)
    listInfo['length'] = calcLengthOfList(arr)
    print(listInfo)
indexInfo([37,2,1,-9])

print("---------------------------------------")
#Reverse List - Create a function that takes a list and return that list with values reversed.
#  Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverseList(arr):
   return list(reversed(arr))
reverseValues = reverseList([37,2,1,-9])
print(reverseValues)


