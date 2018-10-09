if __name__ == "__main__":
    x, y = 0, 0
    steps = 0
    while True:
        dir = input('Your current position is %s, %s, where would you like to move to?' % (str(x), str(y)))
        
        directions = {  'north': (0, 1), 
                        'south' : (0, -1), 
                        'east' : (1, 0), 
                        'west' : (-1, 0)}
               
        if dir in directions:
            print("You moved %s, " % dir)
            x += directions[dir][0]
            y += directions[dir][1]
            steps += 1
            
        elif dir == "leave"
            print("Goodbye. You moved %s steps in total." % steps)
        
        else:
            print("You tried to move %s but that is not possible." % dir)