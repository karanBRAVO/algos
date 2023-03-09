def minimumTime(time: list, totalTrips: int) -> int:
    t = 0
    tripCount = 0
    while tripCount < totalTrips:
        tripCount = 0
        t += 1
        for T in time:
            tripCount += t // T
        print(f"tripcount: {tripCount}, t: {t}")
    return t


time = [3, 3, 8]
totalTrips = 8
print(minimumTime(time, totalTrips))
