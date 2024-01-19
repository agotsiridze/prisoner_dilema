from __future__ import annotations
from typing import TYPE_CHECKING
from . import rounds
if TYPE_CHECKING:
    from game import Players


class Match:
    def __init__(self,player_1:Players,player_2:Players,rounds_qty:int=100) -> None:
        self.rounds_qty = rounds_qty
        self.p1 = player_1
        self.p2 = player_2
        self.round_choices = None
        
    def __call__(self,):
        for _ in range(self.rounds_qty):
            game_round = rounds.Rounds(self.p1, self.p2)
            self.round_choices = game_round.play_round()
    
    def results(self):
        return {f"{self.p1.name}":self.p1.earning, f"{self.p2.name}":self.p2.earning}
