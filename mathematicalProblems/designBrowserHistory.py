class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = homepage
        self.backArr = []
        self.forwardArr = []

    def visit(self, url: str) -> None:
        self.forwardArr.clear()
        self.backArr.append(self.homepage)
        self.homepage = url

    def back(self, steps: int) -> str:
        index = len(self.backArr) - 1
        page = self.homepage
        if len(self.backArr) > 0:
            while index >= 0:
                page = self.backArr[index]
                self.forwardArr.append(self.homepage)
                self.backArr.remove(page)
                self.homepage = page
                if index == len(self.backArr) - steps + 1:
                    break
                index -= 1
                steps -= 1
        return page

    def forward(self, steps: int) -> str:
        index = len(self.forwardArr) - 1
        page = self.homepage
        if len(self.forwardArr) > 0:
            while index >= 0:
                page = self.forwardArr[index]
                self.backArr.append(self.homepage)
                self.forwardArr.remove(page)
                self.homepage = page
                if index == len(self.forwardArr) - steps + 1:
                    break
                index -= 1
                steps -= 1
        return page


# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]

# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]