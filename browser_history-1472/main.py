class BrowserHistory:
    def __init__(self, homepage: str):
        self.backk = [homepage]
        self.forwardd = []

    def visit(self, url: str) -> None:
        self.backk.append(url)
        self.forwardd = []
        
    def back(self, steps: int) -> str:
        while steps >0 and len(self.backk)>1:
            url = self.backk.pop()
            self.forwardd.append(url)
            steps -=1
        return self.backk[-1]
        
    def forward(self, steps: int) -> str:
        while steps >0 and self.forwardd:
            url = self.forwardd.pop()
            self.backk.append(url)
            steps -=1
        return self.backk[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.backk(steps)
# param_3 = obj.forwardd(steps)