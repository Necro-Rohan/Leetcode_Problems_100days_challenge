class RandomizedSet:

    def __init__(self):
        self.new_set = set()
        
    def insert(self, val: int) -> bool:
        first_len = len(self.new_set)
        self.new_set.add(val)
        second_len = len(self.new_set)
        if second_len == first_len:
            return False
        else:
            return True
        
    def remove(self, val: int) -> bool:
        first_len = len(self.new_set)
        self.new_set.discard(val)
        second_len = len(self.new_set)
        if second_len == first_len:
            return False
        else:
            return True
        
    def getRandom(self) -> int:
        import random
        return random.choice(list(self.new_set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()