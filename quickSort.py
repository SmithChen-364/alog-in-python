#quickSort
def quickSort(numarray,start,end):
    if(start>=end):
        return
    forward=start+1
    reverse=end
    while forward<=reverse:
        if(numarray[forward]<numarray[start]):
            forward=forward+1
            continue
        if(numarray[reverse]<numarray[start]):
            numarray[forward],numarray[reverse]=numarray[reverse],numarray[forward]
            forward=forward+1
        else:
            reverse=reverse-1
            continue
    numarray[start],numarray[reverse]=numarray[reverse],numarray[start]
    quickSort(numarray,start,reverse-1)
    quickSort(numarray,reverse+1,end)    
    
array=eval(input("input your list please!"))
quickSort(array,0,len(array)-1)
print("complete")
