#!/usr/bin/env python -tt
 
import pickle
import random, sys
from time import sleep
def get_stopwords(stopchance):
    stopwords = {
        "and":stopchance,
        "with":stopchance,
        "of":stopchance,
        "a":stopchance,
        "the":stopchance,
        "notes":stopchance,
        "to":stopchance,
        "fresh":stopchance,
        "this":stopchance,
        "in":stopchance,
        "on":stopchance,
        "by":stopchance,
        "finish":stopchance,
        "flavors":stopchance,
        "finishing":stopchance
    }
    return stopwords


chain = pickle.load(open("chain.p", "rb"))
 
new_review = []
sword1 = "BEGIN"
sword2 = "NOW"

stopchance = 1.0;
stopwords = get_stopwords(stopchance)
stopreduce = 1.2;

out = " Reduced Chance of '{}' to {}"

while True:

    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])

    if sword2 == "END":
        print ' '.join(new_review)
        new_review = []
        sword1 = "BEGIN"
        sword2 = "NOW"
        stopwords = get_stopwords(stopchance)
        continue;

    if sword2 in stopwords:

        if random.random() < int( stopwords.get(sword2) ):
            
            stopwords[sword2] = stopwords.get(sword2)/stopreduce;
            #print >> sys.stderr, out.format(sword2,  str( stopwords.get(sword2) ))

        else:
            continue;

    new_review.append(sword2)

