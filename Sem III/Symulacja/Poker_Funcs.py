import random as r  
from itertools import combinations  
from collections import Counter 
import itertools

def rank_hand(hand: tuple) -> tuple:
        """
        Evaluates the rank of a poker hand.
        :param hand: A 5-card hand.
        :return: A tuple representing the rank of the hand.
        """
        # Extract values and suits from the hand.
        values = sorted([card[1] for card in hand], reverse=True)
        suits = [card[0] for card in hand]
        value_counts = Counter(values)  # Count occurrences of each value.
        unique_values = sorted(value_counts.values(), reverse=True)

        # Check for flush (all cards have the same suit).
        is_flush = len(set(suits)) == 1
        # Check for straight (consecutive values).
        is_straight = all(values[i] - 1 == values[i + 1] for i in range(len(values) - 1)) or values == [14, 5, 4, 3, 2]
        highest_value = max(values)  # Highest card value.

        # Determine the hand's rank based on poker rules.
        if is_straight and is_flush:
            return (8, highest_value)  # Straight Flush
        elif unique_values == [4, 1]:
            return (7, value_counts.most_common(1)[0][0])  # Four of a Kind
        elif unique_values == [3, 2]:
            return (6, value_counts.most_common(1)[0][0])  # Full House
        elif is_flush:
            return (5, values)  # Flush
        elif is_straight:
            return (4, highest_value)  # Straight
        elif unique_values == [3, 1, 1]:
            return (3, value_counts.most_common(1)[0][0])  # Three of a Kind
        elif unique_values == [2, 2, 1]:
            return (2, value_counts.most_common(2)[0][0], value_counts.most_common(2)[1][0])  # Two Pair
        elif unique_values == [2, 1, 1, 1]:
            return (1, value_counts.most_common(1)[0][0])  # One Pair
        else:
            return (0, values)  # High Card

def best_hand(cards: list):
    """
    Finds the best 5-card hand from 7 cards.
    :param cards: A list of 7 cards (hole cards + table cards).
    :return: The best 5-card hand.
    """
    return max(combinations(cards, 5), key=rank_hand)

def compare_hands(players: list, table_cards: list, n_players : int, not_palying_players : list):
    """
    Compares players' hands based on their best possible poker hand.
    :param players_cards: A dictionary mapping players to their hole cards.
    :param table_cards: The community cards on the table.
    :return: A tuple containing players' ranks and their best hands.
    """
    

    # Map players to their best hands and ranks.
    players_best_hands = {}
    players_rank = {}
    for i in range(n_players):
        if i not in not_palying_players:
            player = f'player {i+1}'
            players_best_hands[player] = best_hand(players[i].cards + table_cards)
            players_rank[player] = rank_hand(players_best_hands[player])

    return players_rank, players_best_hands

def find_winning_player(players_rank: dict, players_best_hands: dict):
    """
    Determines the winning player based on their hand ranks.
    :param players_rank: A dictionary mapping players to their hand ranks.
    :param players_best_hands: A dictionary mapping players to their best hands.
    :return: The winning player's details or a tie.
    """

    def hand_name(rank : tuple) -> str:
        """
        Maps hand ranks to their corresponding poker hand names.
        :param rank: A rank tuple.
        :return: The name of the poker hand.
        """
        names = {
            8: "Straight Flush",
            7: "Four of a Kind",
            6: "Full House",
            5: "Flush",
            4: "Straight",
            3: "Three of a Kind",
            2: "Two Pair",
            1: "One Pair",
            0: "High Card"
        }
        return names[rank[0]]

    # Identify the highest rank.
    highest_rank = max(players_rank.values())

    # Find all players with the highest rank.
    highest_players = [key[-1:] for key, value in players_rank.items() if value == highest_rank]
    
    if len(highest_players) > 1:
        # If there's a tie, return all tied players.
        return f"It's a tie: Players {', '.join(map(str, highest_players))} win", players_best_hands[f'player {highest_players[0]}'], hand_name(highest_rank), highest_players
    else:
        # Otherwise, declare a single winner.
        return f"Player {highest_players[0]} wins", players_best_hands[f'player {highest_players[0]}'], hand_name(highest_rank), int(highest_players[0])

def Poker_odds_calculator(my_hand, table_cards):
    # Define all suits and ranks
    suits = ['spade', 'heart', 'diamond', 'club']
    ranks = list(range(1, 14))  # 2-10, 11(J), 12(Q), 13(K), 14(A)

    # Generate the full deck and exclude cards in my_hand and table_cards
    full_deck = [(suit, rank) for suit in suits for rank in ranks]
    known_cards = set(my_hand + table_cards)
    remaining_deck = [card for card in full_deck if card not in known_cards]

    # Ensure the table has at least 5 cards by adding combinations from the remaining deck
    num_needed = 5 - len(table_cards)
    possible_boards = itertools.combinations(remaining_deck, num_needed)

    # Helper functions to evaluate poker hands
    def is_flush(cards):
        suit_counts = Counter(suit for suit, _ in cards)
        return any(count >= 5 for count in suit_counts.values())

    def is_straight(cards):
        card_ranks = sorted(set(rank for _, rank in cards))
        for i in range(len(card_ranks) - 4):
            if card_ranks[i:i + 5] == list(range(card_ranks[i], card_ranks[i] + 5)):
                return True
        return False

    def is_straight_flush(cards):
        for suit in suits:
            suited_cards = [rank for s, rank in cards if s == suit]
            if is_straight([(suit, rank) for rank in suited_cards]):
                return True
        return False

    def classify_hand(cards):
        """Classify the best hand from 7 cards"""
        card_ranks = sorted((rank for _, rank in cards), reverse=True)
        rank_counts = Counter(card_ranks)
        most_common = rank_counts.most_common()

        if is_straight_flush(cards):
            return "Straight flush"
        if most_common[0][1] == 4:
            return "Four-of-a-Kind"
        if most_common[0][1] == 3 and most_common[1][1] >= 2:
            return "Full house"
        if is_flush(cards):
            return "Flush"
        if is_straight(cards):
            return "Straight"
        if most_common[0][1] == 3:
            return "Three-of-a-Kind"
        if most_common[0][1] == 2 and most_common[1][1] == 2:
            return "Two pair"
        if most_common[0][1] == 2:
            return "One pair"
        return "High card"

    # Simulate possible outcomes
    total_simulations = 0
    hand_counts = Counter()

    for extra_cards in possible_boards:
        all_cards = my_hand + table_cards + list(extra_cards)
        best_hand = classify_hand(all_cards)
        hand_counts[best_hand] += 1
        total_simulations += 1

    # Calculate percentages
    hand_odds = {hand: (hand_counts[hand] / total_simulations) * 100 for hand in [
        "Straight flush", "Four-of-a-Kind", "Full house", "Flush", 
        "Straight", "Three-of-a-Kind", "Two pair", "One pair", "High card"]}

    return hand_odds

 