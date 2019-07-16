#heap sort
def heapSort(numarray):
    numarray.insert(0,0)
    n=len(numarray)

    for x in range(1,n):
        up(numarray,x)

    while n>2:
        numarray[1],numarray[n-1]=numarray[n-1],numarray[1]
        n=n-1
        down(numarray,1,n-1)
    return numarray[-1:0:-1]
def up(numarray,index):
    if(index==1):
        return
    else:
        parentIndex=int(index/2)
        if(numarray[parentIndex]>numarray[index]):
            numarray[parentIndex],numarray[index]=numarray[index],numarray[parentIndex]
            up(numarray,parentIndex)
        
def down(numarray,index,n):#reference to Programming Pearls
    leftchildIndex=2*index
    if(leftchildIndex>n):
        return
    if(leftchildIndex+1<=n):
        if(numarray[leftchildIndex+1]<numarray[leftchildIndex]):
            leftchildIndex=leftchildIndex+1
    if(numarray[index]>numarray[leftchildIndex]):
        numarray[index],numarray[leftchildIndex]=numarray[leftchildIndex],numarray[index]
        down(numarray,leftchildIndex,n)
array=eval(input("input your list to be sorted"))
array=heapSort(array)
print(array)
