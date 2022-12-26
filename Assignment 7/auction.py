# Assignment 7, Task 4
# Name: Chirasak Au Yeung
# Collaborators:
# Time Spent:


from typing import List


class Bid:
    def __init__(self, bid_id, bidder_id, auction):
        self.bid_id = bid_id
        self.bidder_id = bidder_id
        self.auction = auction

    def __str__(self):
        # return a string representation of this bid
        return f"Bid({self.bid_id}, {self.bidder_id}, {self.auction})"

    def __repr__(self):
        # return a string representation of this bid that can be used to
        # recreate an instance of this class
        return self.__str__()

    def __lt__(self, other):
        # return True if this bid's bid_id is less than the other bid's bid_id,
        # and False otherwise
        return self.bid_id < other.bid_id

    def __le__(self, other):
        # return True if this bid's bid_id is less than or equal to the other bid's bid_id,
        # and False otherwise
        return self.bid_id <= other.bid_id

    def __eq__(self, other):
        # return True if this bid's bid_id is equal to the other bid's bid_id,
        # and False otherwise
        return self.bid_id == other.bid_id

    def __ne__(self, other):
        # return True if this bid's bid_id is not equal to the other bid's bid_id,
        # and False otherwise
        return self.bid_id != other.bid_id

    def __gt__(self, other):
        # return True if this bid's bid_id is greater than the other bid's bid_id,
        # and False otherwise
        return self.bid_id > other.bid_id

    def __ge__(self, other):
        # return True if this bid's bid_id is greater than or equal to the other bid's bid_id,
        # and False otherwise
        return self.bid_id >= other.bid_id


class Auction:
    def __init__(self, auction_id):
        self.auction_id = auction_id
        self.price = 1
        self.winner = None

    def placeBid(self, bidder_id):
        # increase the price of this auction by $1.5 and set the winner to the bidder
        # with the specified bidder_id
        self.price += 1.5
        self.winner = bidder_id

    def __str__(self):
        # return a string representation of this auction
        return f"Auction({self.auction_id}, {self.price}, {self.winner})"

    def __repr__(self):
        # return a string representation of this auction that can be used to
        # recreate an instance of this class
        return self.__str__()


def CSV2List(csvFilename: str) -> List[Bid]:
    # create an empty list of bids
    bids = []

    # open the file in read mode
    with open(csvFilename, 'r') as csvFile:
        # read the first line of the file (the header)
        header = csvFile.readline().strip().split(',')

        # for each line in the file (excluding the header),
        for line in csvFile:
            # split the line into fields
            fields = line.strip().split(',')

            # extract the values for the bid_id, bidder_id, and auction fields
            bid_id = fields[header.index('bid_id')]
            bidder_id = fields[header.index('bidder_id')]
            auction = fields[header.index('auction')]

            # create a new Bid instance with the extracted values
            bid = Bid(bid_id, bidder_id, auction)

            # add the bid to the list of bids
            bids.append(bid)

    # sort the list of bids by their bid_id, in ascending order
    bids.sort()

    # return the list of bids
    return bids


def mostPopularAuction(bids: List[Bid]) -> set[str]:
    # create a dictionary to keep track of the number of bidders for each auction
    bidders_count = {}

    # iterate over the bids in the list
    for bid in bids:
        # get the auction identifier for this bid
        auction_id = bid.auction

        # get the number of bidders for this auction, or 0 if this is the first bid for this auction
        bidders = bidders_count.get(auction_id, 0)

        # add the current bidder to the set of bidders for this auction
        bidders.add(bid.bidder_id)

        # update the dictionary with the new number of bidders for this auction
        bidders_count[auction_id] = bidders

    # find the maximum number of bidders
    max_bidders = max(bidders_count.values())

    # create a set to store the auction identifiers with the maximum number of bidders
    popular_auctions = set()

    # iterate over the auctions in the dictionary
    for auction_id, bidders in bidders_count.items():
        # if the number of bidders for this auction is equal to the maximum,
        # add the auction identifier to the set of popular auctions
        if bidders == max_bidders:
            popular_auctions.add(auction_id)

    # return the set of popular auctions
    return popular_auctions


def auctionWinners(bids: List[Bid]) -> dict[str, Auction]:
    # create a dictionary of auctions, where the keys are the auction identifiers
    # and the values are the Auction instances
    auctions = placeBids(bids)

    # create an empty dictionary to store the results
    winners = {}

    # iterate over the auctions in the dictionary
    for auction_id, auction in auctions.items():
        # add the auction to the results dictionary
        winners[auction_id] = auction

    # return the dictionary of auction winners
    return winners
