wordLen = 3  # set the word length accroding to words in given list
lst = ["cat", "rat", "mat", "bat", "run", "fun", "bun"]  # all should have equal length

def swap(arr, i):
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp

def dictSorting(lst):
    for passCount in range(0, len(lst) - 1):
        for index in range(0, len(lst) - passCount - 1):
            for wordIndex in range(0, wordLen):
                if lst[index][wordIndex] > lst[index + 1][wordIndex]:
                    swap(lst, index)
                    break
                elif lst[index][wordIndex] < lst[index + 1][wordIndex]:
                    break
                elif lst[index][wordIndex] == lst[index + 1][wordIndex]:
                    continue

if __name__ == "__main__":
    dictSorting(lst)
    print(lst)

