#!/usr/bin/env python -tt
 
import pickle
import random
 
chain = pickle.load(open("chain.p", "rb"))
 
new_review = []
sword1 = "BEGIN"
sword2 = "NOW"

andchance=100;

while True:
    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
    if sword2 == "END":
        break
    if sword2 == "and":
        if random.random() < int(andchance):
            andchance = andchance/2;
        else:
            continue;

    new_review.append(sword2)

print ' '.join(new_review)