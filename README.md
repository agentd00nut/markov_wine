# markov_wine
95% of the code was used from here http://www.onthelambda.com/2014/02/20/how-to-fake-a-sophisticated-knowledge-of-wine-with-markov-chains/

All I've done is updated the xpath selector.  Munged around with the process.sh script and tried to improve the review generation.


How to use
==========
As of /1/18/17 the wine-reviews.txt and chain.p are up to date.  This means you can just run `python build_review.py` to generate a review.

If you want to update the library run `./process.sh`... Try to be nice to winespectator.com and either add a sleep in the get-reviews script or
don't do this very often!

Improvements
============

All I've done is reduced the chance that the word "and" is a valid choice more than once in any given review.
Each time "and" is picked it's chances of being used in the review again are halved.

This avoids sentences like `Full-bodied, with fine focus and its broad, intense and vivid, with a tangy, lip-smacking profile.`
Amazingly this tiny modification seems to have improved the results drastically.

Todo
======
Analyze, in some way, a large volume of the generated reviews to identify other stop words (and, or, the, of), that appear
more frequently than one would expect from a real sentence.

Get other data sets and see where it takes us.

Potentially add a "negation" effect on certain key words.  We shouldn't use "sweet" if we've already picked "dry", the blog post touched on this.
