import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dictionary = {}

    def insert(self, val):
        if(val in self.dictionary):
            return False
        
        self.arr.append(val)
        self.dictionary[val] = len(self.arr) - 1
        return True
    

    def remove(self, val):
        if(val not in self.dictionary):
            return False
        
        idx = self.dictionary[val]
        last_ele = self.arr[-1]

        self.arr[idx] = last_ele
        self.dictionary[last_ele] = idx

        self.arr.pop()
        del self.dictionary[val]
        return True

    def search(self, val):
        if self.dictionary[val]:
            return True
        return False
    
    def getRandom(self):
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()