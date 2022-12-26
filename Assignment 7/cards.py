# Assignment 7, Task 2
# Name: Chirasak Au Yeung
# Collaborators:
# Time Spent:
# from itertools import combinations
from datetime import datetime

Hand = set[tuple[str, str]]


def is_straight_flush(h: Hand) -> bool:
    cards = list(h)
    suits = [card[1] for card in cards]
    if len(set(suits)) == 1:
        ranks = [card[0] for card in cards]
        ranks.sort()
        if ranks == list(range(ranks[0], ranks[0] + 5)):
            return True
    return False


def is_four_of_a_kind(h: Hand) -> bool:
    rank_counts = {}
    for card in h:
        rank = card[0]
        if rank not in rank_counts:
            rank_counts[rank] = 0
        rank_counts[rank] += 1
    return any(count == 4 for count in rank_counts.values())


def is_full_house(h: Hand) -> bool:
    cards = list(h)
    rank_counts = {}
    for card in cards:
        rank = card[0]
        if rank not in rank_counts:
            rank_counts[rank] = 0
        rank_counts[rank] += 1
    # Check if any rank appears three times and another rank appears two times in the hand
    return any(count == 3 for count in rank_counts.values()) and any(count == 2 for count in rank_counts.values())


def is_two_pair(h: Hand) -> bool:
    cards = list(h)
    rank_counts = {}
    for card in cards:
        rank = card[0]
        if rank not in rank_counts:
            rank_counts[rank] = 0
        rank_counts[rank] += 1
    # Check if any rank appears twice and another rank also appears twice in the hand
    return any(count == 2 for count in rank_counts.values()) and len(
        [count for count in rank_counts.values() if count == 2]) >= 2


start_time = datetime.now()
print(all_hands())
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


def all_hands() -> list[Hand]:
    suits = ["Club", "Diamond", "Heart", "Spade"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards = [(suit, rank) for suit in suits for rank in ranks]
    hands = []
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                for l in range(k + 1, len(cards)):
                    for m in range(l + 1, len(cards)):
                        hand = [cards[i], cards[j], cards[k], cards[l], cards[m]]
                        hands.append(hand)
    return hands


def all_straight_flush() -> list[Hand]:
    hands = all_hands()
    return [hand for hand in hands if is_straight_flush(hand)]


def all_four_of_a_kind() -> list[Hand]:
    hands = all_hands()
    return [hand for hand in hands if is_four_of_a_kind(hand)]


def all_full_house() -> list[Hand]:
    hands = all_hands()
    return [hand for hand in hands if is_full_house(hand)]


def all_two_pair() -> list[Hand]:
    hands = all_hands()
    return [hand for hand in hands if is_two_pair(hand)]
