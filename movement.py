if __name__ == "__main__":
    x, y = 0, 0
    steps = 0
    while True:
        dir = input('Your current position is %s, %s, where would you like to move to? ' % (str(x), str(y)))
        
        directions = { 'north': (0, 1), 
                        'south' : (0, -1), 
                        'east' : (1, 0), 
                        'west' : (-1, 0)}
                        
        abb_directions = {'n': (0, 1), 
                        's' : (0, -1), 
                        'e' : (1, 0), 
                        'w' : (-1, 0)}
        
        long_directions = {'n' : 'north', 's' : 'south', 'e' : 'east', 'w' : 'west'}
        
        dir = dir.lower().replace(" ", "")      
        if dir in directions:
            print("You moved %s. " % dir)
            x += directions[dir][0]
            y += directions[dir][1]
            steps += 1
        
        elif dir in abb_directions:
            print("You moved %s. " % long_directions[dir])
            x += abb_directions[dir][0]
            y += abb_directions[dir][1]
            steps += 1
        
        elif dir == "leave":
            print("Goodbye. You moved %s steps in total." % steps)
            break
        
        else:
            print("You tried to move %s but that is not possible." % dir)