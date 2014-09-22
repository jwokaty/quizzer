#!/bin/usr/env python
"""
Flash card quiz script based on https://openhatch.org/wiki/Flash_card_challenge.
"""

import random
import sys

def main(path):
    """ Reads in cards from file and runs quiz. """
    try:
        with open(path.strip()) as file:
            lines = file.read()[:-1]
    except:
       print "Couldn't read file. Is the file path for the cards correct?" 
       sys.exit()

    cards = [] 

    for line in lines.split('\n'):
        qa = line.split(',')
        cards.append([qa[0].strip(), qa[1].strip()])

    max = len(cards)
    studied_cards = []
    score = 0
    total = 0

    print "Type the correct answer or 'exit' to quit." 

    while True:
        n = random.randrange(0, max)
        if not n in studied_cards:
            studied_cards.append(n)
            answer = raw_input(cards[n][0] + ": ")
            total += 1
            if answer.strip().lower() == cards[n][1].lower():
                score += 1
                print "Correct. Yay!", 
            elif answer.strip().lower() == 'exit':
                print "Goodbye."
                break
            else:
                print "Try again. The correct answer is %s." % cards[n][1],
            print "%d out of %d." % (score, total) 
            if len(studied_cards) == max:
                studied_cards = [] 

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
