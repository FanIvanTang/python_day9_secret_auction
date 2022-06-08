import os


def max_bidding(bidding):

    max_price = float("-inf")
    winner = ""

    for this_name in bidding:
        if bidding[this_name] > max_price:
            winner = this_name
            max_price = bidding[this_name]

    return winner, max_price


from art import logo

if __name__ == "__main__":

    if os.name == "nt":
        clear = lambda: os.system("cls")
    else:
        clear = lambda: os.system("clear")

    print(logo)

    bids = dict()

    end_bid = False

    while not end_bid:

        name = input("What is you name?: ")
        bid = float(input("What is your bid: $"))

        bids[name] = bid

        is_other = input("Are there any other bidders? Type 'yes' or 'no'. ")

        if is_other == "no":
            end_bid = True

        clear()

    winner_name, winner_price = max_bidding(bidding=bids)

    print(f"The winner is {winner_name} with a bid of ${winner_price}")

    # clear()
