from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
	highest_bid = 0
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount == highest_bid:
			highest_bid = bid_amount
			print(f"{winner} bid {highest_bid} before {bidder}")
		elif bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of {highest_bid}")
	exit()


print("Welcome to the bidding website")

while not bidding_finished:
	name = str(input("What is your name?: \n"))
	price = float(input("What is your bid?: $ \n"))
	bids[name] = price
	keep_Playing = input("Is there any other bidder?").lower()
	if keep_Playing == "yes":
		clear()
	else:
		bidding_Finished = True
		find_highest_bidder(bids)
