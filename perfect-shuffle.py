# -*- coding: utf-8 -*-

import sys
import argparse
import colorama

colorama.init()

class Deck(object):
    def __init__(self, num_cards):
        self.num_cards = num_cards
        self.cards = [i for i in range(self.num_cards)]

    def __eq__(self, other):
        return self.cards == other.cards

    def faro_shuffle(self, shuffle_type):
        '''Shuffles the deck using a perfect faro shuffle.'''
        r = []
        for (a, b) in zip(self.cards[0:self.num_cards/2], self.cards[self.num_cards/2:]):
            if shuffle_type == 'out':
                r.append(a)
                r.append(b)
            else:
                r.append(b)
                r.append(a)
        self.cards = r

    def write(self):
        sys.stdout.write('    ')
        for i in range(self.num_cards):
            if self.cards[i] < self.num_cards / 2:
                sys.stdout.write("%s%3d " % (colorama.Fore.RED, self.cards[i]))
            else:
                sys.stdout.write("%s%3d " % (colorama.Fore.GREEN, self.cards[i]))
            #if i == self.num_cards / 2 - 1:
                #sys.stdout.write('\n    ')
        print colorama.Fore.RESET + '\n'

def parse_args():
    desc = 'A simple utility for playing with perfect in/out Faro shuffles'

    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('shuffle_type', action='store', help='Type of shuffle [in|out]')
    parser.add_argument('num_cards', action='store', type=int, help='Number of cards to shuffle')

    args = parser.parse_args()
    return args

def shuffle_till_equal(shuffle_type, num_cards):
    original_deck = Deck(num_cards)  # A deck in new-deck-order we will use for comparison.
    shuffled_deck = Deck(num_cards)  # A deck we will repeatedly perfect faro-shuffle.

    print '\nNew deck:\n'
    original_deck.write()
    print
     
    print 'Shuffling:\n'
    for i in range(1, 1000):
        shuffled_deck.faro_shuffle(shuffle_type)
        shuffled_deck.write()
        if shuffled_deck == original_deck:
            return i
    
    return 0

if __name__ == '__main__':
    args = parse_args()
    
    num_shuffles = shuffle_till_equal(args.shuffle_type, args.num_cards)
    if num_shuffles > 0:
        print("\nDeck is back in new-deck order after %s shuffles." % num_shuffles)
    else:
        print('\nERROR: gave up after 1000 shuffles')
        
