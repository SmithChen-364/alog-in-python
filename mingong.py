map=[]
flag=False
def create_map():
    for x in range(8):
        map.append([0 for x in range(8)])
    for x in range(8):
        map[x][0]=1
        map[0][x]=1
        map[x][7]=1
        map[7][x]=1
    map[3][1]=1
    map[3][2]=1
    map[2][2]=1
    map[6][7]=0
    map[5][3]=1
    map[4][4]=1 
    map[1][4]=1
    map[2][4]=1
    map[3][4]=1
def show_map():
    for x in range(8):
        for y in range(8):
            print(map[x][y],end=" ")
        print()
def find_way(this_map,i,j):
    namespace=False
    #success
    if(i==6 and j==7):
        map[i][j]=2
        return True
    if(map[i+1][j]==0 and namespace==False):
        map[i][j]=2
        namespace=find_way(this_map,i+1,j)
    if(map[i][j+1]==0 and namespace==False):
        map[i][j]=2
        namespace=find_way(this_map,i,j+1)

    if(map[i-1][j]==0 and namespace==False):
        map[i][j]=2
        namespace=find_way(this_map,i-1,j)
    if(map[i][j-1]==0 and namespace==False):
        map[i][j]=2
        namespace=find_way(this_map,i,j-1)
    if(not namespace):
        map[i][j]=3
    
    return namespace  
    
create_map()
show_map()
print("begin run")
find_way(map,1,1)
show_map()


            
