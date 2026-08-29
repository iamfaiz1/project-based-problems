class ATM:

    def __init__(self):
        self.notes = [20, 50, 100, 200, 500]
        self.count = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        result = [0] * 5

        # Start from largest denomination
        for i in range(4, -1, -1):
            note = self.notes[i]

            take = min(amount // note, self.count[i])

            result[i] = take
            amount -= take * note
            if amount <= 0:
                break

        # Could not make exact amount
        if amount != 0:
            return [-1]

        # Actually remove notes
        for i in range(5):
            self.count[i] -= result[i]

        return result