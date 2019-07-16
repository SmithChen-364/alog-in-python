# insert sort
def insertSort(numarray):
    if(len(numarray)==0):
        print("input your list please!")
    else:
        for i in range(1,len(numarray)):
            for j in range(i):
                if(numarray[i]<numarray[j]):
                    insertNum=numarray[i]
                    numarray[j+1:i+1]=numarray[j:i]
                    numarray[j]=insertNum
array=eval(input("input your list to be sorted"))
insertSort(array)
print("complete")    


