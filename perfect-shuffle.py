# -*- coding: utf-8 -*-

import sys
import colorama

colorama.init()

num_cards = 52

class Deck(object):
    def __init__(self):
        self.cards = [i for i in range(num_cards)]

    def __eq__(self, other):
        return self.cards == other.cards

    def faro_shuffle(self):
        '''Shuffles the deck using a perfect faro shuffle.'''
        r = []
        for (a, b) in zip(self.cards[0:num_cards/2], self.cards[num_cards/2:]):
            r.append(a)
            r.append(b)
        self.cards = r

    def write(self):
        sys.stdout.write('    ')
        for i in range(num_cards):
            if self.cards[i] < num_cards / 2:
                sys.stdout.write("%s%3d " % (colorama.Fore.RED, self.cards[i]))
            else:
                sys.stdout.write("%s%3d " % (colorama.Fore.GREEN, self.cards[i]))
        print colorama.Fore.RESET
 
original_deck = Deck()  # A deck in new-deck-order we will use for comparison.
shuffled_deck = Deck()  # A deck we will repeatedly faro-shuffle.

print '\nNew deck:\n'
original_deck.write()
print
 
print 'Shuffling:\n'
for i in range(1, 1000):
    shuffled_deck.faro_shuffle()
    shuffled_deck.write()
    if shuffled_deck == original_deck:
        print("\nDeck is back in new-deck order after %s shuffles." % i)
        break

