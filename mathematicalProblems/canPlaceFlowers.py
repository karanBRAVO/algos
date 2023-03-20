def canPlaceFlowers(flowerbed, n: int) -> bool:
    if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 0:
        return True
    canPlace = False
    placedCount = 0
    for i in range(0, len(flowerbed), 1):
        if flowerbed[i] == 0:
            if i > 0 and i < len(flowerbed) - 1:
                if flowerbed[i + 1] == 0:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        placedCount += 1
            elif i == 0:
                if flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    placedCount += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    placedCount += 1
        if placedCount == n:
            canPlace = True
            break
    print(flowerbed)
    return canPlace


arr = []
for i in input().split():
    arr.append(int(i))
n = int(input("Enter the value of n: "))

print(canPlaceFlowers(flowerbed=arr, n=n))
