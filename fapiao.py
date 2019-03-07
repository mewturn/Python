import random
import time

def generateNumbers(digit):
    return "".join([str(random.randint(0, 9)) for i in range(digit)])

def generatePrizeStatistics(prizes):
    output = {}
    for prize in prizes:
        if prize in output:
            output[prize] += 1
        else:
            output[prize] = 1
    return output

def matchFapiao(number_of_fapiaos, printOutput=False):
    # Modify these variables
    prizes = {"specialprize": 10_000_000, "grandprize": 2_000_000, "firstprize": 200_000, "secondprize": 40_000, "thirdprize": 10_000, "fourthprize": 4_000, "fifthprize": 1_000, "sixthprize": 200}
    additional = 3

    # Generate winning numbers
    specialprize = generateNumbers(8)
    grandprize = generateNumbers(8)
    firstprize = [generateNumbers(8) for i in range(3)]
    secondprize = [i[1:] for i in firstprize]
    thirdprize = [i[2:] for i in firstprize]
    fourthprize = [i[3:] for i in firstprize]
    fifthprize = [i[4:] for i in firstprize]
    sixthprize = [i[5:] for i in firstprize]
    additional_sixthprize = [generateNumbers(3) for i in range(additional)]

    # Counters
    prizes_won = []
    amount_won = 0

    # Generate fapiaos
    fapiaos = [generateNumbers(8) for i in range(number_of_fapiaos)]

    if printOutput:
        print(f"Winning numbers\n----------------\nSpecial Prize: {specialprize}\nGrand Prize: {grandprize}\nFirst Prizes: {(firstprize)}\nAdditional Sixth Prizes: {(additional_sixthprize)}")

    # Match fapiaos
    for fapiao in fapiaos:
        # Special Prize
        if fapiao == specialprize:
            amount_won += prizes["specialprize"]
            prizes_won.append("specialprize")
            if printOutput:
                print(f"Won the special prize! Fapiao Number: {fapiao}")
            continue

        # Grand Prize
        elif fapiao == grandprize:
            amount_won += prizes["grandprize"]
            prizes_won.append("grandprize")
            if printOutput:
                print(f"Won the grand prize! Fapiao Number: {fapiao}")
            continue

        # First Prize
        elif fapiao in firstprize:
            amount_won += prizes["firstprize"]
            prizes_won.append("firstprize")
            if printOutput:
                print(f"Won the first prize! Fapiao Number: {fapiao}")
            continue

        # Second Prize
        elif fapiao[1:] in secondprize:
            amount_won += prizes["secondprize"]
            prizes_won.append("secondprize")
            if printOutput:
                print(f"Won the second prize! Fapiao Number: {fapiao}")
            continue

        # Third Prize
        elif fapiao[2:] in thirdprize:
            amount_won += prizes["thirdprize"]
            prizes_won.append("thirdprize")
            if printOutput:
                print(f"Won the third prize! Fapiao Number: {fapiao}")
            continue

        # Fourth Prize
        elif fapiao[3:] in fourthprize:
            amount_won += prizes["fourthprize"]
            prizes_won.append("fourthprize")
            if printOutput:
                print(f"Won the fourth prize! Fapiao Number: {fapiao}")
            continue

        # Fifth Prize
        elif fapiao[4:] in fifthprize:
            amount_won += prizes["fifthprize"]
            prizes_won.append("fifthprize")
            if printOutput:
                print(f"Won the fifth prize! Fapiao Number: {fapiao}")
            continue

        # Sixth Prize
        elif fapiao[5:] in sixthprize or fapiao[5:] in additional_sixthprize:
            amount_won += prizes["sixthprize"]
            prizes_won.append("sixthprize")
            if printOutput:
                print(f"Won the sixth prize! Fapiao Number: {fapiao}")
            continue

    if printOutput:
        print (f"Statistics\n----------------\nTotal Fapiaos matched: {number_of_fapiaos}\nTotal winning Fapiaos: {len(prizes_won)}\nTotal amount won: {amount_won}")
    return amount_won, prizes_won

if __name__ == "__main__":
    # Modify these variables
    # 20 dumplings each time, 4 times a week, 8 weeks = 15 x 4 x 8 = 480 dumplings per series
    number_of_fapiaos = 40

    number_of_trials = 10_000
    checkpoints = 10
    interval = int(number_of_trials/checkpoints)

    # Chewing gum = NT$ 10
    # 八方雲集 dumpling = NT$ 5
    fapiao_price = 5 

    # Initialize variables
    prizes_won = []
    amount_won = 0
    
    current_time = time.time()
    print(f"Starting! Current time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(current_time))}")
    print("Calculating...")
    for i in range(number_of_trials):
        # Print progress every 10%
        if not i == 0 and not i%interval:
            print(f"{i//interval * checkpoints}% completed.")
        _ = matchFapiao(number_of_fapiaos)
        amount_won += _[0]
        prizes_won += _[1]

    amount_spent = number_of_fapiaos*number_of_trials*fapiao_price
    net_gain = amount_won - amount_spent


    elapsed_time = time.time() - current_time
    print(f"Completed! Elapsed time: {elapsed_time:,.1f}s")

    # Output
    print("------------------------\nTotal statistics\n------------------------")
    print(f"Amount spent: ${amount_spent:,d}")
    print(f"Amount won: ${amount_won:,d} \nPrizes won: {generatePrizeStatistics(prizes_won)}")
    print(f"Net gain: ${net_gain:,d}")
    # print("------------------------\nAverage statistics (per series)\n------------------------")
    # print(f"Average amount spent: ${amount_spent/number_of_trials:,.0f}")
    # print(f"Average amount won: ${amount_won/number_of_trials:,.0f}")
    # print(f"Average net gain: NT${net_gain/number_of_trials:,.0f}")