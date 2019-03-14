from itertools import combinations
from collections import Counter


class Card:
    def __init__(self, card_string):
        self.value = card_string[0]
        self.suit = card_string[1]

    def __repr__(self):
        return '{}{}'.format(self.value, self.suit)


class Hand:
    def __init__(self, five_cards):
        self.five_cards = five_cards

    def __str__(self):
        return "{} {} {} {} {}".format(*self.five_cards)

    def values(self):
        return [card.value for card in self.five_cards]

    def suits(self):
        return [card.suit for card in self.five_cards]

    def is_royal_flush(self):
        return all(i in self.values() for i in ['T', 'J', 'Q', 'K', 'A']) and \
               5 in Counter(self.suits()).values()

    def is_four_of_a_kind(self):
        return 4 in Counter(self.values()).values()

    def is_full_house(self):
        return all(i in Counter(self.values()).values() for i in [2, 3])

    def is_flush(self):
        return 5 in Counter(self.suits()).values()

    def is_straigt(self):
        all_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        for i in range(10):
            # Loop through the first 10 sequential elements of all_values
            # and see if the currents Hands values are completely in any of those sets
            # and also check if all the values in the current hand are unique
            if all(value in all_values[i:i + 5] for value in self.values()) and \
                    len(self.values()) == len(set(self.values())):
                return True
        return False

    def is_three_of_a_kind(self):
        return 3 in Counter(self.values()).values()

    def is_two_pairs(self):
        return 2 == list(Counter(self.values()).values()).count(2)

    def is_one_pair(self):
        return 1 == list(Counter(self.values()).values()).count(2)

    def rank(self):
        """returns weighted rank of Hand, with 0 being the best hand """
        if self.is_royal_flush():
            return 0
        elif self.is_four_of_a_kind():
            return 1
        elif self.is_full_house():
            return 2
        elif self.is_flush():
            return 3
        elif self.is_straigt():
            return 4
        elif self.is_three_of_a_kind():
            return 5
        elif self.is_two_pairs():
            return 6
        elif self.is_one_pair():
            return 7
        else:  # Highest card if nothing else :(
            return 8


class PokerHandAdvisor:
    hand_ranks = [
        'royal-flush',
        'four-of-a-kind',
        'full-house',
        'flush',
        'straight',
        'three-of-a-kind',
        'two-pairs',
        'one-pair',
        'highest-card']

    def __init__(self, cards_string):
        all_ten_cards = [Card(card_string) for card_string in cards_string.split(' ')]
        self.hand = all_ten_cards[:5]
        self.deck = all_ten_cards[5:]
        self.all_possible_hand_ranks = [Hand(self.hand).rank()]

    def __str__(self):
        return ""

    def take_cards_from_the_top_of_the_deck(self, number_of_cards):
        return self.deck[:number_of_cards]

    def new_possible_hand(self, card_indexes_to_take_out):
        remaining_cards = [card for index, card in enumerate(self.hand) if index not in card_indexes_to_take_out]
        new_cards = self.take_cards_from_the_top_of_the_deck(len(card_indexes_to_take_out))
        return Hand(remaining_cards + new_cards)

    def generate_all_possibilities_of_hands(self):
        for number_of_cards_to_remove in range(1, 6):
            list_of_card_indexes_to_take_out = list(
                combinations(list(range(5)), number_of_cards_to_remove))
            for card_indexes_to_take_out in list_of_card_indexes_to_take_out:
                new_possible_hand = self.new_possible_hand(card_indexes_to_take_out)
                self.all_possible_hand_ranks.append(new_possible_hand.rank())

    def pick_best_hand(self):
        """sort the list of all possible hand ranks and pick the first (highest) value"""
        all_possible_hand_rank_values = sorted(self.all_possible_hand_ranks)
        return "Hand: {} Deck: {} Best hand: {}".format(
            str(Hand(self.hand)), 
            str(Hand(self.deck)), 
            self.hand_ranks[all_possible_hand_rank_values[0]])

    def best_hand(self):
        self.generate_all_possibilities_of_hands()
        return self.pick_best_hand()



if __name__ == '__main__':
    p = PokerHandAdvisor('TH JH QC QD QS QH KH AH 2S 6S')
    print(p.best_hand())

    p = PokerHandAdvisor('2H 2S 3H 3S 3C 2D 3D 6C 9C TH')
    print(p.best_hand())

    p = PokerHandAdvisor('2H 2S 3H 3S 3C 2D 9C 3D 6C TH')
    print(p.best_hand())

    p = PokerHandAdvisor('2H AD 5H AC 7H AH 6H 9H 4H 3C')
    print(p.best_hand())

    p = PokerHandAdvisor('AC 2D 9C 3S KD 5S 4D KS AS 4C')
    print(p.best_hand())

    p = PokerHandAdvisor('KS AH 2H 3C 4H KC 2C TC 2D AS')
    print(p.best_hand())

    p = PokerHandAdvisor('AH 2C 9S AD 3C QH KS JS JD KD')
    print(p.best_hand())

    p = PokerHandAdvisor('6C 9C 8C 2D 7C 2H TC 4C 9S AH')
    print(p.best_hand())

    p = PokerHandAdvisor('3D 5S 2H QD TD 6S KH 9H AD QH')
    print(p.best_hand())










