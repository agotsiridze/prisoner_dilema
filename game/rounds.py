from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Players
    
class Rounds:
    def __init__(self,p1:Players, p2:Players)->None:
        self.p1 = p1
        self.p2 = p2
    
        
    def _reward_players(self, p1_reward:int,p2_reward:int):
        self.p1.score=p1_reward
        self.p2.score=p2_reward
        
        
    def play_round(self):
        p1_choice=self.p1.choose()
        p2_choice=self.p2.choose()
        if (p1_choice==True and p2_choice==True):
            self._reward_players(3,3)
        elif (p1_choice and not(p2_choice)):
            self._reward_players(0,5)
        elif (p2_choice and not(p1_choice)):
            self._reward_players(5,0)
        else:
            self._reward_players(1,1)
        return {self.p1.name: p1_choice, self.p2.name: p2_choice}
   

