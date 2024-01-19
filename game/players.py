from random import getrandbits

class Players:
    def __init__(self, name:str) -> None:
        self.name = name
        self._score=0
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,amount):
        self._score += amount

    def choose(self)->bool:
        user_input = self.user_input()
        if type(user_input)==bool:
            return user_input
        else:
            raise TypeError("User input must be a boolean")

    @staticmethod
    def user_input()->bool:
        """
        It is Random for now
        """
        return bool(getrandbits(1))
    
    def __repr__(self) -> str:
        return self.name
    
    def __iter__(self):
        return iter({"name":self.name, "score":self._score}.items())
    