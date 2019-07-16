#KMP算法程序
import time

next_array=[]
backpoint=0
def init_array(word):
    for x in range(len(word)):
        next_array.append(-1)
    next_array[0]=0
def get_next(backpoint,word):
    for prepoint in range(1,len(word)):
        if(word[prepoint]==word[backpoint]):
            next_array[prepoint]=next_array[prepoint-1]+1
            backpoint=backpoint+1
        else:
            while(backpoint>0 and word[prepoint]!=word[backpoint]):
                backpoint=next_array[backpoint-1]
            next_array[prepoint]=backpoint
def print_array():
    print(next_array)
def measure_time(func):
    def inner(word,search_word):
        a=time.time()
        func(word,search_word)
        b=time.time()
        print(b-a)
    return inner
@measure_time
def KMP_begin_search(word,search_word):
    i=0
    j=0
    count=0
    Flag=False
    while(i<len(word)):
        if(search_word[j]==word[i]):
            j=j+1
            i=i+1
            if(j==len(search_word)):
                Flag=True
                break
        else:
            if(j==0):
                i=i+1
            j=next_array[j-1]
        count=count+1
    print("KMP's count is %s"%count)
    if(not Flag):
        print("Failed")
    else:
        print("OK")
@measure_time
def BF_begin_search(word,search_word):
    i=0
    j=0
    count=0
    Flag=False
    while(i<len(word)):
        count=count+1
        if(word[i]==search_word[j]):
            j=j+1
            i=i+1
            if(j==len(search_word)):
                Flag=True
                break
        else:
            i=i-j+1
            j=0
            
    if(Flag):
        print("OK")
    else:
        print("Failed")
    print("count is %s"%count)
    

word=input("input your string")
search_word=input("input your search_string") 
init_array(search_word)
get_next(0,search_word)
print_array()
print("KMP:__________")
KMP_begin_search(word,search_word)
print("BF:,_______")
BF_begin_search(word,search_word)


            
    
    
