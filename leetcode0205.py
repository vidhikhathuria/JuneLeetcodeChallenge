# Problem Link : https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:
    from collections import defaultdict
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.arr = list()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val] = 1
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            del self.d[val]
            idx = self.arr.index(val)
            self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = int(random.random() * len(self.arr))
        return self.arr[idx]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()