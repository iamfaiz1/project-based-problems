# python implementation

class SeatManager:
    import heapq
    def __init__(self, n: int):
        self.arr = [i for i in range(1, n+1)]
        heapq.heapify(self.arr)

        # number : index
        self.di = {}

    def reserve(self) -> int:
        if self.arr:
            seat = heapq.heappop(self.arr)
            self.di[seat] = seat-1
            return seat
        else:
            return -1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.arr, seatNumber)
        del self.di[seatNumber]


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)