myStr = "qwertyuioplkjhgfdsazxcvbnm"

lst = []
for char in myStr:
    lst.append(char)
    
newStr = ""

for k in range(0, len(lst)):
    for i in range(0, len(lst) - (k + 1)):
        if lst[i] > lst[i + 1]:
            temp = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = temp

for char in lst:
    newStr += char

print(newStr)