def defangIPaddr(address: str) -> str:
    newStr = ""
    for i in range(0, len(address)):
        if address[i] != '.':
            newStr += address[i]
        elif address[i] == '.':
            newStr += f"[{address[i]}]"
    return newStr


addr = "255.100.89.90"
print(defangIPaddr(address=addr))
