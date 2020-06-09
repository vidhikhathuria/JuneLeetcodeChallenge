# Problem Link : https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        li = []
        people = sorted(people, key=lambda x: (-x[0],x[1]))
        for i in people:
            li.insert(i[1], i)
        return li