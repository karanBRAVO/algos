lst = ["windowspowershell", "computer", "chrome", "pycharm", "vscode", "androidstudio",
       "intellijidea", "mozilla", "edge", "anaconda", "linux", "unix", "windows", "explorer", "commandpromp", "weather", "xboxgamebar", "firefox", "google", "microsoft", "apple", "git", "github", "Gitlab", "mysql", "docker", "metamask"]


def swap(arr: list, i: int):
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp


def dictSorting(lst: list):
    for passCount in range(0, len(lst) - 1):
        for index in range(0, len(lst) - passCount - 1):
            for wordIndex in range(0, len(lst[index])):
                try:
                    if lst[index][wordIndex].lower() == lst[index + 1][wordIndex].lower():
                        continue
                    elif lst[index][wordIndex].lower() < lst[index + 1][wordIndex].lower():
                        break
                    elif lst[index][wordIndex].lower() > lst[index + 1][wordIndex].lower():
                        swap(lst, index)
                        break
                except IndexError:
                    if len(lst[index]) > len(lst[index + 1]):
                        swap(lst, index)
                        break


if __name__ == "__main__":
    dictSorting(lst)
    print(lst)
