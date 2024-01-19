from game import Players, Match
from itertools import combinations



ROUNDS_QTY = 100
PRISONERS_QTY = 10

prisoners = [Players(f"P{i}") for i in range(PRISONERS_QTY)]


for p1, p2, in combinations(prisoners,2):
    play = Match(p1, p2, rounds_qty=ROUNDS_QTY)
    choices = play()
    

winners = sorted(prisoners, key=lambda x: x.score, reverse=True)

print("================================")
for prisoner in winners:
    print(dict(prisoner))