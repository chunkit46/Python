from typing import List, Dict


def winner(records: List[Dict[str, int]]) -> str:
    # Create a dictionary with the names of the players as keys and their points as values
    points = {}
    for record in records:
        # For each match record, update the points of the players
        for player, wins in record.items():
            if player not in points:
                points[player] = 0
            # If a player wins 2 or 3 games in a match, they earn 1 point
            if wins >= 2:
                points[player] += 1

    # Find the player with the most points
    max_points = 0
    winner = ""
    for player, p in points.items():
        if p > max_points:
            max_points = p
            winner = player
        # If there is a tie, return an empty string
        elif p == max_points:
            winner = ""

    return winner


# Chess
assert winner([{'A': 2, 'B': 1}]) == 'A'
assert winner([{'A': 3, 'B': 0}, {'A': 1, 'C': 2}]) == ''
assert winner([{'A': 3, 'B': 0}, {'A': 1, 'C': 2}, {'B': 0, 'C': 3}]) == 'C'
assert winner([{'A': 3, 'B': 0}, {'A': 1, 'C': 2}, {'B': 0, 'D': 3}, {'A': 2, 'D': 1}]) == 'A'
assert winner([{'A': 3, 'B': 0}, {'B': 2, 'C': 1}, {'C': 2, 'D': 1}, {'A': 0, 'D': 3}]) == ''
