#Merge Sort
def mergeSort(numarray,start,end):
    if(start<end):
        mid=int((start+end)/2)
        mergeSort(numarray,start,mid)
        mergeSort(numarray,mid+1,end)
        merge(numarray,start,mid,end)
def merge(_numarray,start,mid,end):
    tempArray=[]
    i=start
    j=mid+1
    while(i<=mid and j<=end):
        if(_numarray[i]<_numarray[j]):
            tempArray.append(_numarray[i])
            i=i+1
        else:
            tempArray.append(_numarray[j])
            j=j+1
    if(i>mid):
        tempArray.extend(_numarray[j:end+1])
    else:
        tempArray.extend(_numarray[i:mid+1])
    _numarray[start:end+1]=tempArray
array=eval(input("input your list to be sorted"))
mergeSort(array,0,len(array)-1)
print(array)

