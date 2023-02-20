numberOfInputs = int(input("~ Enter the input count: "))

totalSum = 0
digitCount = 10
for i in range(0, numberOfInputs):
    number = int(input(f"~ {i + 1} Enter the number: "))
    totalSum += number

print(f'first 10 digits are {str(totalSum)[0:digitCount]}')
