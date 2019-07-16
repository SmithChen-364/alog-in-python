#汉诺塔程序
plate_number=5
def play_game(plate_number,a,b,c):
    if(plate_number==1):
        print("from "+a+" to "+c)
    else:
        play_game(plate_number-1,a,c,b)
        play_game(1,a,b,c)
        play_game(plate_number-1,b,a,c)
play_game(plate_number,"A","B","C")    
    
