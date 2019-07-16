#count sort
def countSort(numarray):
    maxNumber=max(max(numarray)+1,len(numarray))
    countArray=[0 for x in range(maxNumber)]
    print(countArray)
    for i in numarray:
        countArray[i]=countArray[i]+1
    numarray=[]
    for j in range(len(countArray)):
        if(countArray[j]!=0):
            for count in range(countArray[j]):
                numarray.append(j)
    return numarray
array=eval(input("input your data to be sorted"))
array=countSort(array)
print(array)

