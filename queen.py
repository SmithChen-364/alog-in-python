#八皇后的Python程序
max_number=10
index_array=[]
def init_array():
    for x in range(max_number):
        index_array.append(-1)
def clear():
    for x in range(len(index_array)):
        index_array[x]=-1
def print_array():
    print(index_array)

def start_game(index):
    if(index==max_number):
        print_array()
    else:
        for x in range(max_number):
            index_array[index]=x
            if(not is_conflict(index)):
                start_game(index+1)
def is_conflict(index):
    for x in range(index):
        if(index_array[index]==index_array[x] or abs(index_array[index]-index_array[x])==abs(index-x)):
            return True
    return False
init_array()
print_array()
start_game(0)

                

        

