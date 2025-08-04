# empty dictionary
dictionary = {}

flag = True

while flag:
    name = input("What is your name? ")
    bid = input("What is your bid? ")

    dictionary[name] = bid

    another_participant = input("Is there anyone else to participate? (yes/no) ")

    print("\n " * 100)

    if another_participant.lower() != "yes":
        flag = False

all_bids = list(dictionary.values())
highest_bid = max(all_bids)

highest_bid = 0
winner_name = ""

for name, bid in dictionary.items():
    if int(bid) > highest_bid:
        highest_bid = int(bid)
        winner_name = name

print(f"Winner: {winner_name} with bid: {highest_bid}")
