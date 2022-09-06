def GetPairsCount(arr, num, sum):
 
    count = 0
    for i in range(0, num):
        
        n = len(arr)

        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
arr = []
num=int(input("Number of elements in array is : "))
for i in range(0,num):
   length=int(input("Enter the element is :" ))
   arr.append(length)
print(arr)
num = len(arr)
sum = int(input("Enter the sum is :" ))
print("Count of pairs is", GetPairsCount(arr, num, sum))