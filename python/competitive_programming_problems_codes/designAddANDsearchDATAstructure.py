class WordDictionary:
    def __init__(self):
        self.dictArr = []

    def addWord(self, word: str) -> None:
        self.dictArr.append(word)

    def search(self, word: str) -> bool:
        isPresent = False
        for ele in self.dictArr:
            if ele == word:
                return True
            for i in range(len(word)):
                if word[i] == ".":
                    isPresent = True
                    continue
                if len(word) == len(ele):
                    if word[i] == ele[i]:
                        isPresent = True
                    else:
                        isPresent = False
                        break
                else:
                    isPresent = False
                    break
            if isPresent:
                return isPresent
        return isPresent


word = WordDictionary()
word.addWord("addword")
word.addWord("addword")
print(word.dictArr)
print(word.search("."))
print(word.search("a"))
print(word.search("aa"))
print(word.search("a"))
print(word.search(".a"))
print(word.search("a."))

# ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
# [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
