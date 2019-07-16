#Bubble Sort
def bubbleSort(numarray):
    if(len(numarray)==0):
        print("input your list please!")
    else:
        for i in range(len(numarray)-1):
            for j in range(len(numarray)-1,i,-1):
                if(numarray[j]<numarray[j-1]):
                    numarray[j],numarray[j-1]=numarray[j-1],numarray[j]
array=eval(input("input your list"))
bubbleSort(array)
print("complete")
