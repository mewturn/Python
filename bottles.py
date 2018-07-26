import sys

def count(bottle, empty=0, caps=0):
    empty_per_bottle = 4
    cap_per_bottle = 2
    if bottle == 0 and empty < empty_per_bottle and caps < cap_per_bottle:
        print("Empty Bottles: %s Bottle Caps: %s" %(empty, caps))
        return 0        
    empty = bottle + empty
    bottles_from_empty = int(empty/empty_per_bottle)
    caps = bottle + caps
    bottles_from_cap = int(caps/cap_per_bottle)
    return bottle + count(bottles_from_empty + bottles_from_cap, empty%empty_per_bottle, caps%cap_per_bottle)


if __name__ == "__main__":
    while True:
        bottles = input("Please enter the number of bottles of beer bought initially: ")
        print("Total bottles of beer drunk:", count(int(bottles)))