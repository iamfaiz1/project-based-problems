"""
    we can take the range between 100 to 1000, but we will take 100 because the number of elements in the hashset is less than 10^4 and the average number of elements in each bucket will be less than 100. ( i just assumed it.)
    if i took a range greater than 1000, the run time goes around 2000+ ms and if i took even bigger range 10000000 i got memory limit exceeded error. so i took 100 as the range.
"""
class MyHashSet:

    def __init__(self):
        self.bucket = [[] for _ in range(100)]


    def add(self, key: int) -> None:
        idx = key % len(self.bucket)
        if key not in self.bucket[idx]:
            self.bucket[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.bucket)
        if key in self.bucket[idx]:
            self.bucket[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx = key % len(self.bucket)
        return key in self.bucket[idx]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)