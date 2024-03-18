# max_spanning_tree.py

An implementation of the Chu Liu Edmonds Algorithm. https://en.wikipedia.org/wiki/Edmonds%27_algorithm

Created as part of my ongoing learning in the NLP space - this algorithm is often useful in dependency parsing as described by Martin and Jurafsky: https://web.stanford.edu/~jurafsky/slp3/18.pdf

There is one modification to the algorithm. In this implementation, the graph is not fully contracted and expanded when a cycle is found. Instead, the algorithm searches for the cycle's appropriate new incoming edge, deletes the cycle-making edge,
then performs the recursion.
